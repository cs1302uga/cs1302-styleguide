# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "coverage",
# ]
# ///
"""Unit tests for etc/check_sync.py."""

from __future__ import annotations

import io
import os
import shutil
import sys
import tempfile
import unittest
from unittest import mock

# Ensure 'etc' is on sys.path for importing check_sync and build_readme
ETC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "etc"))
if ETC_DIR not in sys.path:
    sys.path.insert(0, ETC_DIR)

import build_readme
import check_sync


class TestCheckSync(unittest.TestCase):
    """Test suite for check_sync functions and CLI."""

    def setUp(self) -> None:
        """Create temporary workspace directory and silence stdout/stderr."""
        self.stdout_patcher = mock.patch("sys.stdout", new_callable=io.StringIO)
        self.stderr_patcher = mock.patch("sys.stderr", new_callable=io.StringIO)
        self.mock_stdout = self.stdout_patcher.start()
        self.mock_stderr = self.stderr_patcher.start()

        self.test_dir = tempfile.TemporaryDirectory()
        self.root = self.test_dir.name
        self.etc_dir = os.path.join(self.root, "etc")
        self.guidelines_dir = os.path.join(self.root, "guidelines")
        os.makedirs(self.etc_dir, exist_ok=True)
        os.makedirs(self.guidelines_dir, exist_ok=True)

        self.xml_path = os.path.join(self.root, "cs1302_checks.xml")
        with open(self.xml_path, "w", encoding="utf-8") as f:
            f.write(
                """<?xml version="1.0"?>
                <module name="Checker">
                    <module name="TreeWalker">
                        <module name="AlphaName"/>
                        <module name="BetaName"/>
                    </module>
                </module>
                """
            )

        self.preamble_path = os.path.join(self.etc_dir, "README_preamble.md")
        with open(self.preamble_path, "w", encoding="utf-8") as f:
            f.write("# Title\n\n<!-- TOC_PLACEHOLDER -->\n\n## Specific Guidelines\n\nNotes.\n")

        self.postamble_path = os.path.join(self.etc_dir, "README_postamble.md")
        with open(self.postamble_path, "w", encoding="utf-8") as f:
            f.write("## References\n\n* Ref 1\n")

        # Create guidelines
        for name in ["AlphaName", "BetaName", "CheckStyleException"]:
            folder = os.path.join(self.guidelines_dir, name)
            os.makedirs(folder, exist_ok=True)
            with open(
                os.path.join(folder, "README.md"),
                "w",
                encoding="utf-8",
            ) as f:
                f.write(f"### {name}\n\nDescription.\n")

        # Build initial synchronized README.md
        build_readme.build_readme(repo_root=self.root)

    def tearDown(self) -> None:
        """Clean up temporary test workspace directory and restore streams."""
        self.test_dir.cleanup()
        self.stdout_patcher.stop()
        self.stderr_patcher.stop()

    def test_extract_readme_guideline_headers_success(self) -> None:
        """Tests extraction of guideline headers from valid README.md."""
        readme_path = os.path.join(self.root, "README.md")
        headers = check_sync.extract_readme_guideline_headers(readme_path)
        self.assertEqual(headers, ["AlphaName", "BetaName", "CheckStyleException"])

    def test_extract_readme_guideline_headers_not_found(self) -> None:
        """Tests FileNotFoundError when README does not exist."""
        with self.assertRaises(FileNotFoundError):
            check_sync.extract_readme_guideline_headers(
                os.path.join(self.root, "missing.md")
            )

    def test_extract_readme_toc_guidelines_success(self) -> None:
        """Tests extraction of guideline entries from TOC."""
        readme_path = os.path.join(self.root, "README.md")
        toc = check_sync.extract_readme_toc_guidelines(readme_path)
        self.assertEqual(toc, ["AlphaName", "BetaName", "CheckStyleException"])

    def test_extract_readme_toc_guidelines_not_found(self) -> None:
        """Tests FileNotFoundError when README does not exist for TOC extraction."""
        with self.assertRaises(FileNotFoundError):
            check_sync.extract_readme_toc_guidelines(
                os.path.join(self.root, "missing.md")
            )

    def test_check_synchronization_success(self) -> None:
        """Tests that full synchronization check passes on clean repo."""
        is_valid, errors = check_sync.check_synchronization(self.root)
        self.assertTrue(is_valid)
        self.assertEqual(errors, [])

    def test_check_synchronization_xml_error(self) -> None:
        """Tests error reporting when XML is invalid/missing."""
        os.remove(self.xml_path)
        is_valid, errors = check_sync.check_synchronization(self.root)
        self.assertFalse(is_valid)
        self.assertTrue(any("Failed to parse XML" in e for e in errors))

    def test_check_synchronization_guidelines_dir_error(self) -> None:
        """Tests error reporting when guidelines directory is missing."""
        invalid_root = os.path.join(self.root, "sub")
        os.makedirs(invalid_root)
        # copy xml only
        with open(os.path.join(invalid_root, "cs1302_checks.xml"), "w") as f:
            f.write("<module name='Checker'/>")
        is_valid, errors = check_sync.check_synchronization(invalid_root)
        self.assertFalse(is_valid)
        self.assertTrue(any("Failed to read guidelines directory" in e for e in errors))

    def test_check_synchronization_missing_in_guidelines(self) -> None:
        """Tests reporting when an active XML module lacks a guideline file."""
        shutil.rmtree(os.path.join(self.guidelines_dir, "AlphaName"))
        is_valid, errors = check_sync.check_synchronization(self.root)
        self.assertFalse(is_valid)
        self.assertTrue(any("Active XML modules missing" in e for e in errors))

    def test_check_synchronization_extra_in_guidelines(self) -> None:
        """Tests reporting when extra unconfigured guideline file exists."""
        folder = os.path.join(self.guidelines_dir, "ExtraName")
        os.makedirs(folder, exist_ok=True)
        with open(
            os.path.join(folder, "README.md"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write("### ExtraName\n")
        is_valid, errors = check_sync.check_synchronization(self.root)
        self.assertFalse(is_valid)
        self.assertTrue(any("Extra files in guidelines" in e for e in errors))

    def test_check_synchronization_missing_readme_file(self) -> None:
        """Tests error when README.md is missing."""
        os.remove(os.path.join(self.root, "README.md"))
        is_valid, errors = check_sync.check_synchronization(self.root)
        self.assertFalse(is_valid)
        self.assertTrue(any("Failed to read README.md" in e for e in errors))

    def test_check_synchronization_readme_header_discrepancy(self) -> None:
        """Tests detection of missing and extra headers in README.md."""
        readme_path = os.path.join(self.root, "README.md")
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Replace BetaName header with UnrelatedHeader
        content = content.replace("### BetaName", "### UnrelatedHeader")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)

        is_valid, errors = check_sync.check_synchronization(self.root)
        self.assertFalse(is_valid)
        self.assertTrue(any("missing from README.md section headers" in e for e in errors))
        self.assertTrue(any("contains headers not in guidelines" in e for e in errors))

    def test_check_synchronization_unordered_headers(self) -> None:
        """Tests detection of out-of-order section headers in README.md."""
        readme_path = os.path.join(self.root, "README.md")
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Swap order of AlphaName and BetaName headers
        content = content.replace("### AlphaName\n\nDescription.\n\n### BetaName", "### BetaName\n\nDescription.\n\n### AlphaName")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)

        is_valid, errors = check_sync.check_synchronization(self.root)
        self.assertFalse(is_valid)
        self.assertTrue(any("sections in README.md are not in alphabetical order" in e for e in errors))

    def test_check_synchronization_toc_discrepancy(self) -> None:
        """Tests detection of TOC entry omissions and ordering issues."""
        readme_path = os.path.join(self.root, "README.md")
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Alter TOC line
        content = content.replace("* [AlphaName](#alphaname)", "* [ZetaName](#zetaname)")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)

        is_valid, errors = check_sync.check_synchronization(self.root)
        self.assertFalse(is_valid)
        self.assertTrue(any("missing from README.md Table of Contents" in e for e in errors))
        self.assertTrue(any("Table of Contents guideline entries in README.md are not in alphabetical order" in e for e in errors))

    def test_check_synchronization_toc_extraction_error(self) -> None:
        """Tests error handling when README extraction fails during TOC check."""
        with mock.patch("check_sync.extract_readme_toc_guidelines", side_effect=ValueError("TOC failure")):
            is_valid, errors = check_sync.check_synchronization(self.root)
            self.assertFalse(is_valid)
            self.assertTrue(any("Failed to extract TOC" in e for e in errors))

    def test_main_success(self) -> None:
        """Tests CLI main when synchronization passes."""
        exit_code = check_sync.main(["--repo-root", self.root])
        self.assertEqual(exit_code, 0)

    def test_main_failure(self) -> None:
        """Tests CLI main when synchronization fails."""
        shutil.rmtree(os.path.join(self.guidelines_dir, "AlphaName"))
        exit_code = check_sync.main(["--repo-root", self.root])
        self.assertEqual(exit_code, 1)

    def test_run_as_script(self) -> None:
        """Tests executing check_sync as __main__ using runpy."""
        import runpy

        script_path = os.path.join(ETC_DIR, "check_sync.py")
        # Ensure ETC_DIR is removed from sys.path to exercise import path insertion
        if ETC_DIR in sys.path:
            sys.path.remove(ETC_DIR)
        with mock.patch(
            "sys.argv",
            ["check_sync.py", "--repo-root", self.root],
        ):
            with self.assertRaises(SystemExit) as ctx:
                runpy.run_path(script_path, run_name="__main__")
            self.assertEqual(ctx.exception.code, 0)
        # Restore ETC_DIR to sys.path
        if ETC_DIR not in sys.path:
            sys.path.insert(0, ETC_DIR)


if __name__ == "__main__":
    unittest.main()
