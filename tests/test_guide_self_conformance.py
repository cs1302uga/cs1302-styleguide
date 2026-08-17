# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "coverage",
# ]
# ///
"""Unit tests for self-conformance of guideline example code.

Discovers Java example files placed in guidelines/<Module>/valid/ and
guidelines/<Module>/invalid/ and verifies that:
  1. Valid example files pass check1302 with 0 violations.
  2. Invalid example files fail check1302 and report the expected [Module] error.
Supports intelligent content-addressable caching to skip re-auditing unchanged code.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from typing import Any, Callable, Dict, List, Optional, Tuple

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GUIDELINES_DIR = os.path.join(REPO_ROOT, "guidelines")
CHECKS_XML = os.path.join(REPO_ROOT, "cs1302_checks.xml")
TEMPLATE_PATH = os.path.join(REPO_ROOT, "etc", "check_template.sh")
DEFAULT_CACHE_PATH = os.path.join(REPO_ROOT, ".cache", "style_conformance_cache.json")


def compute_file_sha256(file_path: str) -> str:
    """Computes the SHA-256 hexadecimal digest of a file.

    Args:
        file_path: Path to the target file.

    Returns:
        Hexadecimal SHA-256 digest string, or empty string if file does not exist.
    """
    if not os.path.isfile(file_path):
        return ""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


class ConformanceCache:
    """Persistent cache for style check audit results."""

    def __init__(
        self,
        cache_path: str = DEFAULT_CACHE_PATH,
        checks_xml_path: str = CHECKS_XML,
        guidelines_dir: str = GUIDELINES_DIR,
    ) -> None:
        """Initializes the conformance cache instance.

        Args:
            cache_path: Filepath where cache json is stored.
            checks_xml_path: Path to cs1302_checks.xml.
            guidelines_dir: Path to guidelines directory.
        """
        self.cache_path = cache_path
        self.checks_xml_path = checks_xml_path
        self.guidelines_dir = guidelines_dir
        self.checks_xml_sha256: str = ""
        self.entries: Dict[str, Dict[str, Any]] = {}
        self.dirty: bool = False

    def load(self) -> None:
        """Loads cached results from disk."""
        if not os.path.isfile(self.cache_path):
            self.checks_xml_sha256 = compute_file_sha256(self.checks_xml_path)
            self.entries = {}
            self.dirty = False
            return

        try:
            with open(self.cache_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.checks_xml_sha256 = data.get("checks_xml_sha256", "")
            self.entries = data.get("entries", {})
            self.dirty = False
        except (json.JSONDecodeError, OSError):
            self.checks_xml_sha256 = compute_file_sha256(self.checks_xml_path)
            self.entries = {}
            self.dirty = False

    def save(self) -> None:
        """Saves current cache entries to disk if modifications were made."""
        if not self.dirty:
            return

        os.makedirs(os.path.dirname(os.path.abspath(self.cache_path)), exist_ok=True)
        current_xml_hash = compute_file_sha256(self.checks_xml_path)
        payload = {
            "version": 1,
            "checks_xml_sha256": current_xml_hash,
            "entries": self.entries,
        }
        tmp_path = f"{self.cache_path}.tmp.{os.getpid()}"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
        os.replace(tmp_path, self.cache_path)
        self.dirty = False

    def is_valid(
        self,
        module_name: str,
        expectation: str,
        java_file_path: str,
    ) -> bool:
        """Determines whether a cached result is valid for a given Java file.

        Args:
            module_name: Guideline module name.
            expectation: 'valid' or 'invalid'.
            java_file_path: Path to the target Java file.

        Returns:
            True if the cached result is present, passed, and all dependent
            files (checks XML, Java file, module README.md) are unchanged.
        """
        if os.environ.get("NO_CACHE") == "1" or os.environ.get("CS1302_NO_CACHE") == "1":
            return False

        current_xml_hash = compute_file_sha256(self.checks_xml_path)
        if not current_xml_hash or current_xml_hash != self.checks_xml_sha256:
            return False

        rel_key = os.path.relpath(java_file_path, REPO_ROOT)
        entry = self.entries.get(rel_key)
        if not entry or not entry.get("passed", False):
            return False

        if entry.get("expectation") != expectation:
            return False

        # Verify Java file content hash
        current_java_hash = compute_file_sha256(java_file_path)
        if not current_java_hash or current_java_hash != entry.get("java_sha256"):
            return False

        # Verify module README.md hash (ensuring code is in sync with documentation)
        readme_path = os.path.join(self.guidelines_dir, module_name, "README.md")
        current_readme_hash = compute_file_sha256(readme_path)
        if not current_readme_hash or current_readme_hash != entry.get("readme_sha256"):
            return False

        return True

    def get_cached_result(self, java_file_path: str) -> Tuple[int, str]:
        """Retrieves cached (exit_code, output) for a Java file."""
        rel_key = os.path.relpath(java_file_path, REPO_ROOT)
        entry = self.entries[rel_key]
        return int(entry["exit_code"]), str(entry["output"])

    def record_result(
        self,
        module_name: str,
        expectation: str,
        java_file_path: str,
        exit_code: int,
        output: str,
        passed: bool,
    ) -> None:
        """Records an audit result into the cache."""
        rel_key = os.path.relpath(java_file_path, REPO_ROOT)
        readme_path = os.path.join(self.guidelines_dir, module_name, "README.md")
        self.checks_xml_sha256 = compute_file_sha256(self.checks_xml_path)
        self.entries[rel_key] = {
            "module_name": module_name,
            "expectation": expectation,
            "java_sha256": compute_file_sha256(java_file_path),
            "readme_sha256": compute_file_sha256(readme_path),
            "exit_code": exit_code,
            "output": output,
            "passed": passed,
        }
        self.dirty = True


def discover_guideline_test_cases(
    guidelines_dir: str,
) -> List[Tuple[str, str, str]]:
    """Discovers all valid and invalid Java example files across guidelines.

    Args:
        guidelines_dir: Root path to the guidelines directory.

    Returns:
        A list of tuples (module_name, expectation, java_file_path) where
        expectation is either 'valid' or 'invalid'.

    Raises:
        FileNotFoundError: If guidelines_dir does not exist.
    """
    if not os.path.isdir(guidelines_dir):
        raise FileNotFoundError(f"Guidelines directory not found: {guidelines_dir}")

    test_cases: List[Tuple[str, str, str]] = []
    for module_name in sorted(os.listdir(guidelines_dir)):
        module_dir = os.path.join(guidelines_dir, module_name)
        if not os.path.isdir(module_dir) or module_name.startswith("."):
            continue

        for expectation in ["valid", "invalid"]:
            sub_dir = os.path.join(module_dir, expectation)
            if os.path.isdir(sub_dir):
                for fname in sorted(os.listdir(sub_dir)):
                    if fname.endswith(".java"):
                        file_path = os.path.join(sub_dir, fname)
                        test_cases.append((module_name, expectation, file_path))

    return test_cases


def render_check_runner(
    template_path: str,
    checks_xml_path: str,
    output_path: str,
    course_num: str = "1302",
    guide_url: str = "https://git.io/Jm9uP",
) -> None:
    """Renders a check script from check_template.sh into the destination path.

    Args:
        template_path: Path to etc/check_template.sh.
        checks_xml_path: Path to cs1302_checks.xml.
        output_path: Path where the rendered executable script will be written.
        course_num: Course number substitution string (default: '1302').
        guide_url: Style guide URL substitution string.

    Raises:
        FileNotFoundError: If template_path or checks_xml_path does not exist.
    """
    if not os.path.isfile(template_path):
        raise FileNotFoundError(f"Template not found: {template_path}")
    if not os.path.isfile(checks_xml_path):
        raise FileNotFoundError(f"Checks XML not found: {checks_xml_path}")

    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()

    rendered = (
        content.replace("@COURSE_NUM@", course_num)
        .replace("@GUIDE_URL@", guide_url)
        .replace("@CHECKS_FILE_PATH@", os.path.abspath(checks_xml_path))
    )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered)

    os.chmod(output_path, 0o755)


def run_style_check(
    runner_path: str,
    checks_xml_path: str,
    java_file_path: str,
) -> Tuple[int, str]:
    """Executes the style checker on a specific Java source file.

    Args:
        runner_path: Path to checkstyle or check1302 executable.
        checks_xml_path: Path to cs1302_checks.xml.
        java_file_path: Path to the .java file to audit.

    Returns:
        A tuple of (exit_code, output_text).
    """
    env = os.environ.copy()
    env["CS1302_CHECKS"] = os.path.abspath(checks_xml_path)

    # Determine invocation arguments
    if os.path.basename(runner_path).startswith("checkstyle"):
        cmd = [runner_path, "-c", os.path.abspath(checks_xml_path), java_file_path]
    else:
        cmd = [runner_path, java_file_path]

    proc = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        env=env,
        check=False,
    )

    return proc.returncode, proc.stdout


class TestGuideSelfConformance(unittest.TestCase):
    """Test suite executing style checks against example code in guidelines/."""

    runner_dir: tempfile.TemporaryDirectory[str] | None = None
    runner_path: str | None = None
    cache: ConformanceCache | None = None

    @classmethod
    def setUpClass(cls) -> None:
        """Locates or renders a check1302 / checkstyle runner and loads cache."""
        cls.cache = ConformanceCache()
        cls.cache.load()

        checkstyle_bin = shutil.which("checkstyle")
        if checkstyle_bin:
            cls.runner_path = checkstyle_bin
        elif os.path.isfile(TEMPLATE_PATH) and os.path.isfile(CHECKS_XML):
            cls.runner_dir = tempfile.TemporaryDirectory()
            rendered = os.path.join(cls.runner_dir.name, "check1302")
            render_check_runner(TEMPLATE_PATH, CHECKS_XML, rendered)
            cls.runner_path = rendered

    @classmethod
    def tearDownClass(cls) -> None:
        """Cleans up temporary runner executable and saves cache entries."""
        if cls.cache:
            cls.cache.save()
        if cls.runner_dir:
            cls.runner_dir.cleanup()

    def test_compute_file_sha256_not_found(self) -> None:
        """Tests that compute_file_sha256 returns empty string for missing file."""
        self.assertEqual(compute_file_sha256("/nonexistent_file_xyz"), "")

    def test_conformance_cache_corrupted_file(self) -> None:
        """Tests that ConformanceCache gracefully handles corrupted JSON."""
        with tempfile.TemporaryDirectory() as tmpdir:
            cpath = os.path.join(tmpdir, "corrupt_cache.json")
            with open(cpath, "w", encoding="utf-8") as f:
                f.write("not valid json {")
            cache = ConformanceCache(cache_path=cpath, checks_xml_path=CHECKS_XML)
            cache.load()
            self.assertEqual(cache.entries, {})

    def test_conformance_cache_invalidations(self) -> None:
        """Tests various invalidation scenarios in ConformanceCache."""
        with tempfile.TemporaryDirectory() as tmpdir:
            cpath = os.path.join(tmpdir, "cache.json")
            xml_path = os.path.join(tmpdir, "checks.xml")
            with open(xml_path, "w") as f:
                f.write("<module/>")
            gdir = os.path.join(tmpdir, "guidelines", "Mod")
            os.makedirs(os.path.join(gdir, "valid"), exist_ok=True)
            readme_path = os.path.join(gdir, "README.md")
            with open(readme_path, "w") as f:
                f.write("readme")
            java_path = os.path.join(gdir, "valid", "Ex.java")
            with open(java_path, "w") as f:
                f.write("class Ex {}")

            cache = ConformanceCache(
                cache_path=cpath,
                checks_xml_path=xml_path,
                guidelines_dir=os.path.join(tmpdir, "guidelines"),
            )
            cache.record_result("Mod", "valid", java_path, 0, "Audit done.", True)
            cache.save()

            # Cache hit
            self.assertTrue(cache.is_valid("Mod", "valid", java_path))

            # Expectation mismatch
            self.assertFalse(cache.is_valid("Mod", "invalid", java_path))

            # NO_CACHE bypass
            with unittest.mock.patch.dict(os.environ, {"NO_CACHE": "1"}):
                self.assertFalse(cache.is_valid("Mod", "valid", java_path))

            # Java file modification
            with open(java_path, "w") as f:
                f.write("class ExModified {}")
            self.assertFalse(cache.is_valid("Mod", "valid", java_path))

            # Restore java file, modify README.md
            with open(java_path, "w") as f:
                f.write("class Ex {}")
            with open(readme_path, "w") as f:
                f.write("updated readme")
            self.assertFalse(cache.is_valid("Mod", "valid", java_path))

            # Checks XML modification
            with open(readme_path, "w") as f:
                f.write("readme")
            with open(xml_path, "w") as f:
                f.write("<module name='TreeWalker'/>")
            self.assertFalse(cache.is_valid("Mod", "valid", java_path))

    def test_discover_guideline_test_cases_not_found(self) -> None:
        """Tests that FileNotFoundError is raised for non-existent directory."""
        with self.assertRaises(FileNotFoundError):
            discover_guideline_test_cases("/nonexistent_guidelines_path_xyz")

    def test_render_check_runner_missing_template(self) -> None:
        """Tests FileNotFoundError when template file does not exist."""
        with self.assertRaises(FileNotFoundError):
            render_check_runner(
                "/nonexistent_template.sh",
                CHECKS_XML,
                "/tmp/out.sh",
            )

    def test_render_check_runner_missing_checks(self) -> None:
        """Tests FileNotFoundError when checks XML file does not exist."""
        with self.assertRaises(FileNotFoundError):
            render_check_runner(
                TEMPLATE_PATH,
                "/nonexistent_checks.xml",
                "/tmp/out.sh",
            )

    def test_render_and_run_custom_runner(self) -> None:
        """Tests rendering and invoking a custom runner script."""
        with tempfile.TemporaryDirectory() as tmpdir:
            runner_file = os.path.join(tmpdir, "custom_runner")
            render_check_runner(TEMPLATE_PATH, CHECKS_XML, runner_file)
            self.assertTrue(os.path.isfile(runner_file))
            self.assertTrue(os.access(runner_file, os.X_OK))

            if shutil.which("checkstyle"):
                valid_files = [
                    f
                    for _, exp, f in discover_guideline_test_cases(GUIDELINES_DIR)
                    if exp == "valid"
                ]
                if valid_files:
                    code, _ = run_style_check(runner_file, CHECKS_XML, valid_files[0])
                    self.assertEqual(code, 0)


def _generate_test_method(
    module_name: str, expectation: str, file_path: str
) -> Callable[[TestGuideSelfConformance], None]:
    """Factory creating an individual test method for a discovered Java file.

    Args:
        module_name: Name of the guideline module.
        expectation: Expected result ('valid' or 'invalid').
        file_path: Path to the .java example file.

    Returns:
        A test method bound to the specified test case.
    """

    def test_method(self: TestGuideSelfConformance) -> None:
        is_cached = bool(self.cache and self.cache.is_valid(module_name, expectation, file_path))

        if is_cached and self.cache:
            exit_code, output = self.cache.get_cached_result(file_path)
        else:
            if not self.runner_path:
                self.skipTest("Neither 'checkstyle' nor template available.")

            exit_code, output = run_style_check(
                self.runner_path,
                CHECKS_XML,
                file_path,
            )

        if expectation == "valid":
            passed = exit_code == 0
            if self.cache and not is_cached:
                self.cache.record_result(
                    module_name, expectation, file_path, exit_code, output, passed
                )
            self.assertEqual(
                exit_code,
                0,
                f"Expected valid style in '{file_path}', but check failed:\n{output}",
            )
        else:
            expected_error = f"[{module_name}]"
            passed = exit_code != 0 and expected_error in output
            if self.cache and not is_cached:
                self.cache.record_result(
                    module_name, expectation, file_path, exit_code, output, passed
                )
            self.assertNotEqual(
                exit_code,
                0,
                f"Expected invalid style in '{file_path}', but check passed:\n{output}",
            )
            self.assertIn(
                expected_error,
                output,
                f"Expected violation '{expected_error}' in output for '{file_path}', got:\n{output}",
            )

    rel_path = os.path.relpath(file_path, GUIDELINES_DIR)
    test_method.__doc__ = f"Audits example file: {rel_path} ({expectation})"
    return test_method


# Dynamically register individual test methods for all discovered example files
if os.path.isdir(GUIDELINES_DIR):
    for mod, exp, fpath in discover_guideline_test_cases(GUIDELINES_DIR):
        base_name = os.path.splitext(os.path.basename(fpath))[0]
        test_method_name = f"test_example_{mod}_{exp}_{base_name}"
        setattr(
            TestGuideSelfConformance,
            test_method_name,
            _generate_test_method(mod, exp, fpath),
        )


if __name__ == "__main__":
    unittest.main()
