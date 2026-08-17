# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "coverage",
# ]
# ///
"""Unit tests for etc/build_readme.py."""

from __future__ import annotations

import io
import os
import shutil
import sys
import tempfile
import unittest
from unittest import mock

# Ensure 'etc' is on sys.path for importing build_readme
ETC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "etc"))
if ETC_DIR not in sys.path:
    sys.path.insert(0, ETC_DIR)

import build_readme


class TestBuildReadme(unittest.TestCase):
    """Test suite for build_readme functions and CLI."""

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

        # Setup standard minimal fixtures
        self.xml_path = os.path.join(self.root, "cs1302_checks.xml")
        with open(self.xml_path, "w", encoding="utf-8") as f:
            f.write(
                """<?xml version="1.0"?>
                <module name="Checker">
                    <module name="TreeWalker">
                        <module name="TypeName"/>
                        <module name="MemberName"/>
                        <module name="SuppressionXpathSingleFilter"/>
                        <module/>
                    </module>
                </module>
                """
            )

        self.preamble_path = os.path.join(self.etc_dir, "README_preamble.md")
        with open(self.preamble_path, "w", encoding="utf-8") as f:
            f.write("# Title\n\n<!-- TOC_PLACEHOLDER -->\n\n## Content\n")

        self.postamble_path = os.path.join(self.etc_dir, "README_postamble.md")
        with open(self.postamble_path, "w", encoding="utf-8") as f:
            f.write("## References\n\n* Ref 1\n")

        # Create guidelines
        for name in ["TypeName", "MemberName", "CheckStyleException"]:
            guideline_folder = os.path.join(self.guidelines_dir, name)
            os.makedirs(guideline_folder, exist_ok=True)
            with open(
                os.path.join(guideline_folder, "README.md"),
                "w",
                encoding="utf-8",
            ) as f:
                f.write(f"### {name}\n\nDescription of {name}.\n")

    def tearDown(self) -> None:
        """Clean up temporary test workspace directory and restore streams."""
        self.test_dir.cleanup()
        self.stdout_patcher.stop()
        self.stderr_patcher.stop()

    def test_parse_checkstyle_modules_success(self) -> None:
        """Tests parsing of valid XML with ignored modules and nameless nodes."""
        modules = build_readme.parse_checkstyle_modules(self.xml_path)
        self.assertEqual(modules, ["MemberName", "TypeName"])

    def test_parse_checkstyle_modules_file_not_found(self) -> None:
        """Tests that FileNotFoundError is raised for non-existent XML."""
        with self.assertRaises(FileNotFoundError):
            build_readme.parse_checkstyle_modules(
                os.path.join(self.root, "missing.xml")
            )

    def test_get_available_guidelines_success(self) -> None:
        """Tests scanning guidelines directory and ignoring hidden directories."""
        # Create hidden directory
        hidden_folder = os.path.join(self.guidelines_dir, ".hidden")
        os.makedirs(hidden_folder, exist_ok=True)

        guidelines = build_readme.get_available_guidelines(self.guidelines_dir)
        self.assertIn("TypeName", guidelines)
        self.assertIn("MemberName", guidelines)
        self.assertIn("CheckStyleException", guidelines)
        self.assertNotIn(".hidden", guidelines)

    def test_get_available_guidelines_not_found(self) -> None:
        """Tests that FileNotFoundError is raised for missing guidelines dir."""
        with self.assertRaises(FileNotFoundError):
            build_readme.get_available_guidelines(
                os.path.join(self.root, "nonexistent")
            )

    def test_get_available_guidelines_flat_file_error(self) -> None:
        """Tests that ValueError is raised when a flat file is in guidelines dir."""
        with open(
            os.path.join(self.guidelines_dir, "flat_file.md"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write("flat")
        with self.assertRaises(ValueError) as ctx:
            build_readme.get_available_guidelines(self.guidelines_dir)
        self.assertIn("Expected guideline directory", str(ctx.exception))

    def test_get_available_guidelines_missing_readme(self) -> None:
        """Tests that FileNotFoundError is raised when a folder lacks README.md."""
        empty_folder = os.path.join(self.guidelines_dir, "EmptyGuideline")
        os.makedirs(empty_folder, exist_ok=True)
        with self.assertRaises(FileNotFoundError) as ctx:
            build_readme.get_available_guidelines(self.guidelines_dir)
        self.assertIn("Guideline README.md missing", str(ctx.exception))

    def test_generate_table_of_contents(self) -> None:
        """Tests Table of Contents generation and alphabetical sorting."""
        toc = build_readme.generate_table_of_contents(["ZName", "AName"])
        self.assertIn("## Table of Contents", toc)
        self.assertIn("* [AName](#aname)", toc)
        self.assertIn("* [ZName](#zname)", toc)
        self.assertTrue(toc.index("[AName]") < toc.index("[ZName]"))

    def test_build_readme_content_success(self) -> None:
        """Tests full README content construction with placeholder."""
        content = build_readme.build_readme_content(
            preamble_path=self.preamble_path,
            postamble_path=self.postamble_path,
            guidelines_dir=self.guidelines_dir,
            xml_path=self.xml_path,
        )
        self.assertIn("# Title", content)
        self.assertIn("## Table of Contents", content)
        self.assertIn("### TypeName", content)
        self.assertIn("### MemberName", content)
        self.assertIn("### CheckStyleException", content)
        self.assertIn("## References", content)

    def test_build_readme_content_without_placeholder(self) -> None:
        """Tests fallback concatenation when placeholder is missing."""
        no_placeholder = os.path.join(self.etc_dir, "no_placeholder.md")
        with open(no_placeholder, "w", encoding="utf-8") as f:
            f.write("# Header without tag")

        content = build_readme.build_readme_content(
            preamble_path=no_placeholder,
            postamble_path=self.postamble_path,
            guidelines_dir=self.guidelines_dir,
            xml_path=self.xml_path,
        )
        self.assertIn("# Header without tag", content)
        self.assertIn("## Table of Contents", content)

    def test_build_readme_content_missing_preamble(self) -> None:
        """Tests error when preamble file does not exist."""
        with self.assertRaises(FileNotFoundError):
            build_readme.build_readme_content(
                preamble_path=os.path.join(self.root, "missing_pre.md"),
                postamble_path=self.postamble_path,
                guidelines_dir=self.guidelines_dir,
                xml_path=self.xml_path,
            )

    def test_build_readme_content_missing_postamble(self) -> None:
        """Tests error when postamble file does not exist."""
        with self.assertRaises(FileNotFoundError):
            build_readme.build_readme_content(
                preamble_path=self.preamble_path,
                postamble_path=os.path.join(self.root, "missing_post.md"),
                guidelines_dir=self.guidelines_dir,
                xml_path=self.xml_path,
            )

    def test_build_readme_content_missing_guideline_file(self) -> None:
        """Tests error when an XML module has no corresponding guideline file."""
        shutil.rmtree(os.path.join(self.guidelines_dir, "TypeName"))
        with self.assertRaises(ValueError) as ctx:
            build_readme.build_readme_content(
                preamble_path=self.preamble_path,
                postamble_path=self.postamble_path,
                guidelines_dir=self.guidelines_dir,
                xml_path=self.xml_path,
            )
        self.assertIn("TypeName", str(ctx.exception))

    def test_build_readme_write_mode(self) -> None:
        """Tests write mode of build_readme."""
        out_file = os.path.join(self.root, "README.md")
        result = build_readme.build_readme(
            repo_root=self.root,
            output_path=out_file,
            check_only=False,
        )
        self.assertTrue(result)
        self.assertTrue(os.path.isfile(out_file))

    def test_build_readme_check_mode_matching(self) -> None:
        """Tests check mode when output file is already up to date."""
        out_file = os.path.join(self.root, "README.md")
        build_readme.build_readme(
            repo_root=self.root, output_path=out_file, check_only=False
        )
        result = build_readme.build_readme(
            repo_root=self.root, output_path=out_file, check_only=True
        )
        self.assertTrue(result)

    def test_build_readme_check_mode_out_of_date(self) -> None:
        """Tests check mode when output file is out of date."""
        out_file = os.path.join(self.root, "README.md")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write("Outdated content")

        result = build_readme.build_readme(
            repo_root=self.root, output_path=out_file, check_only=True
        )
        self.assertFalse(result)

    def test_build_readme_check_mode_file_missing(self) -> None:
        """Tests check mode when output file does not exist."""
        out_file = os.path.join(self.root, "missing_README.md")
        result = build_readme.build_readme(
            repo_root=self.root, output_path=out_file, check_only=True
        )
        self.assertFalse(result)

    def test_main_success(self) -> None:
        """Tests CLI main with valid arguments."""
        out_file = os.path.join(self.root, "README.md")
        exit_code = build_readme.main(
            ["--repo-root", self.root, "--output", out_file]
        )
        self.assertEqual(exit_code, 0)
        self.assertTrue(os.path.isfile(out_file))

    def test_main_check_success(self) -> None:
        """Tests CLI main in --check mode when file is matching."""
        out_file = os.path.join(self.root, "README.md")
        build_readme.main(["--repo-root", self.root, "--output", out_file])
        exit_code = build_readme.main(
            ["--repo-root", self.root, "--output", out_file, "--check"]
        )
        self.assertEqual(exit_code, 0)

    def test_main_check_failure(self) -> None:
        """Tests CLI main in --check mode when file is outdated."""
        out_file = os.path.join(self.root, "README.md")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write("wrong")
        exit_code = build_readme.main(
            ["--repo-root", self.root, "--output", out_file, "--check"]
        )
        self.assertEqual(exit_code, 1)

    def test_main_exception_handling(self) -> None:
        """Tests CLI main error handling when invalid root is given."""
        exit_code = build_readme.main(["--repo-root", "/nonexistent_path_xyz"])
        self.assertEqual(exit_code, 1)

    def test_run_as_script(self) -> None:
        """Tests executing build_readme as __main__ using runpy."""
        import runpy

        out_file = os.path.join(self.root, "README.md")
        script_path = os.path.join(ETC_DIR, "build_readme.py")
        with mock.patch(
            "sys.argv",
            ["build_readme.py", "--repo-root", self.root, "--output", out_file],
        ):
            with self.assertRaises(SystemExit) as ctx:
                runpy.run_path(script_path, run_name="__main__")
            self.assertEqual(ctx.exception.code, 0)


if __name__ == "__main__":
    unittest.main()
