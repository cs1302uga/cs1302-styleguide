#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Build and assemble the CSCI 1302 Code Style Guide README.md.

This script parses cs1302_checks.xml and the modular markdown files in
guidelines/ to automatically generate an up-to-date, alphabetized Table of
Contents and complete README.md document.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional, Set

# Structural or filter modules in Checkstyle that do not represent code guidelines.
IGNORED_MODULES: Set[str] = {
    "Checker",
    "TreeWalker",
    "BeforeExecutionExclusionFileFilter",
    "SuppressionXpathSingleFilter",
    "SuppressionFilter",
    "SuppressWithNearbyCommentFilter",
    "SeverityMatchFilter",
}

# Informative sections that are documented but not active Checkstyle XML modules.
INFORMATIVE_GUIDELINES: Set[str] = {
    "CheckStyleException",
}


def parse_checkstyle_modules(xml_path: str) -> List[str]:
    """Parses a Checkstyle XML configuration file for active check modules.

    Args:
        xml_path: Path to the Checkstyle XML configuration file.

    Returns:
        A list of active module names configured in the XML file.

    Raises:
        FileNotFoundError: If xml_path does not exist.
        ET.ParseError: If xml_path contains invalid XML.
    """
    if not os.path.isfile(xml_path):
        raise FileNotFoundError(f"Configuration file not found: {xml_path}")

    tree = ET.parse(xml_path)
    root = tree.getroot()

    modules: List[str] = []
    for elem in root.iter("module"):
        name = elem.attrib.get("name")
        if name and name not in IGNORED_MODULES:
            modules.append(name)

    return sorted(list(set(modules)))


def get_available_guidelines(guidelines_dir: str) -> Dict[str, str]:
    """Reads all guideline markdown files from the specified directory.

    Each guideline must be organized in its own subdirectory containing a
    README.md file (e.g., guidelines/TypeName/README.md).

    Args:
        guidelines_dir: Directory containing individual guideline folders.

    Returns:
        A dictionary mapping guideline name to its markdown content.

    Raises:
        FileNotFoundError: If guidelines_dir does not exist or if a guideline
            directory lacks a README.md file.
        ValueError: If a non-directory file is found directly inside
            guidelines_dir.
    """
    if not os.path.isdir(guidelines_dir):
        raise FileNotFoundError(f"Guidelines directory not found: {guidelines_dir}")

    guidelines: Dict[str, str] = {}
    for entry in sorted(os.listdir(guidelines_dir)):
        if entry.startswith("."):
            continue
        entry_path = os.path.join(guidelines_dir, entry)
        if not os.path.isdir(entry_path):
            raise ValueError(
                f"Expected guideline directory in {guidelines_dir}, found file: {entry_path}"
            )
        readme_path = os.path.join(entry_path, "README.md")
        if not os.path.isfile(readme_path):
            raise FileNotFoundError(
                f"Guideline README.md missing in directory: {entry_path}"
            )
        with open(readme_path, "r", encoding="utf-8") as f:
            guidelines[entry] = f.read().strip()

    return guidelines


def generate_table_of_contents(guideline_names: List[str]) -> str:
    """Generates the Markdown Table of Contents with sorted guideline links.

    Args:
        guideline_names: List of guideline names to include in the TOC.

    Returns:
        The formatted Table of Contents markdown string.
    """
    toc_lines: List[str] = [
        "## Table of Contents",
        "",
        "* [Compliance](#compliance)",
        "* [Motivation](#motivation)",
        "* [When and How to Check](#when-and-how-to-check)",
        "   * [When to Check](#when-to-check)",
        "   * [Run Checkstyle](#run-checkstyle)",
        "   * [Multiple Files](#multiple-files)",
        "   * [Output Examples](#output-examples)",
        "* [Recommended Emacs Configurations](#recommended-emacs-configurations)",
        "   * [Additional Emacs Configurations](#additional-emacs-configurations)",
        "      * [Automatically Update Emacs Packages](#automatically-update-emacs-packages)",
        "      * [Show Style Guide Violations in the Editor](#show-style-guide-violations-in-the-editor)",
        "* [Recommended Vi Configurations](#recommended-vi-configurations)",
        "* [Specific Guidelines](#specific-guidelines)",
    ]

    for name in sorted(guideline_names):
        anchor = name.lower()
        toc_lines.append(f"   * [{name}](#{anchor})")

    toc_lines.extend(
        [
            "* [References](#references)",
            "* [Publication History](#publication-history)",
        ]
    )

    return "\n".join(toc_lines)


def build_readme_content(
    preamble_path: str,
    postamble_path: str,
    guidelines_dir: str,
    xml_path: str,
) -> str:
    """Assembles the complete README.md content from components.

    Args:
        preamble_path: Path to preamble markdown file.
        postamble_path: Path to postamble markdown file.
        guidelines_dir: Directory containing individual guideline markdown files.
        xml_path: Path to cs1302_checks.xml.

    Returns:
        The assembled README.md text content.

    Raises:
        FileNotFoundError: If any required component file is missing.
        ValueError: If guideline files are missing for any active XML module.
    """
    if not os.path.isfile(preamble_path):
        raise FileNotFoundError(f"Preamble file not found: {preamble_path}")
    if not os.path.isfile(postamble_path):
        raise FileNotFoundError(f"Postamble file not found: {postamble_path}")

    configured_modules = set(parse_checkstyle_modules(xml_path))
    available_guidelines = get_available_guidelines(guidelines_dir)

    all_expected_names = configured_modules | INFORMATIVE_GUIDELINES
    missing = all_expected_names - set(available_guidelines.keys())
    if missing:
        missing_list = ", ".join(sorted(missing))
        raise ValueError(
            f"Missing guideline documentation files for: {missing_list}"
        )

    with open(preamble_path, "r", encoding="utf-8") as f:
        preamble_text = f.read().strip()

    with open(postamble_path, "r", encoding="utf-8") as f:
        postamble_text = f.read().strip()

    sorted_names = sorted(list(available_guidelines.keys()))
    toc_text = generate_table_of_contents(sorted_names)

    # Insert generated TOC into preamble placeholder
    if "<!-- TOC_PLACEHOLDER -->" in preamble_text:
        preamble_with_toc = preamble_text.replace(
            "<!-- TOC_PLACEHOLDER -->", toc_text
        )
    else:
        preamble_with_toc = f"{preamble_text}\n\n{toc_text}"

    # Assemble sorted guideline sections
    guideline_sections: List[str] = [
        available_guidelines[name] for name in sorted_names
    ]
    guidelines_body = "\n\n".join(guideline_sections)

    # Final document assembly
    parts = [preamble_with_toc, guidelines_body, postamble_text]
    assembled = "\n\n".join(parts).strip() + "\n"

    return assembled


def build_readme(
    repo_root: str,
    output_path: Optional[str] = None,
    check_only: bool = False,
) -> bool:
    """Builds README.md or verifies that it is up to date.

    Args:
        repo_root: Root directory of the cs1302-styleguide repository.
        output_path: Target path for README.md (defaults to repo_root/README.md).
        check_only: If True, asserts up-to-date status without writing.

    Returns:
        True if check passed or write succeeded; False if check failed.
    """
    preamble_path = os.path.join(repo_root, "etc", "README_preamble.md")
    postamble_path = os.path.join(repo_root, "etc", "README_postamble.md")
    guidelines_dir = os.path.join(repo_root, "guidelines")
    xml_path = os.path.join(repo_root, "cs1302_checks.xml")
    target_output = output_path or os.path.join(repo_root, "README.md")

    generated_content = build_readme_content(
        preamble_path=preamble_path,
        postamble_path=postamble_path,
        guidelines_dir=guidelines_dir,
        xml_path=xml_path,
    )

    if check_only:
        if not os.path.isfile(target_output):
            print(f"Error: Output file does not exist: {target_output}")
            return False
        with open(target_output, "r", encoding="utf-8") as f:
            current_content = f.read()
        if current_content != generated_content:
            print(f"Error: {target_output} is out of date. Run etc/build_readme.py to update.")
            return False
        return True

    with open(target_output, "w", encoding="utf-8") as f:
        f.write(generated_content)

    print(f"Successfully generated: {target_output}")
    return True


def main(argv: Optional[List[str]] = None) -> int:
    """Main CLI entry point for build_readme.py.

    Args:
        argv: Command-line arguments (defaults to sys.argv[1:]).

    Returns:
        0 on success, non-zero on failure.
    """
    parser = argparse.ArgumentParser(
        description="Build or check the CSCI 1302 Code Style Guide README.md."
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Path to repository root (default: current directory).",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Path to output README.md (default: <repo-root>/README.md).",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check whether README.md is up to date without writing.",
    )

    args = parser.parse_args(argv)

    try:
        success = build_readme(
            repo_root=args.repo_root,
            output_path=args.output,
            check_only=args.check,
        )
        return 0 if success else 1
    except Exception as exc:  # pylint: disable=broad-except
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
