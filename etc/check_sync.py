#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Sync and consistency verification linter for CSCI 1302 Style Guide.

Verifies 100% parity and consistency between:
  1. Active Checkstyle modules in cs1302_checks.xml
  2. Guideline definition files in guidelines/*.md
  3. Table of Contents and section headers in README.md
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from typing import List, Optional, Set, Tuple

# Ensure etc directory is on sys.path for direct script execution
ETC_DIR = os.path.dirname(os.path.abspath(__file__))
if ETC_DIR not in sys.path:
    sys.path.insert(0, ETC_DIR)

from build_readme import (
    IGNORED_MODULES,
    INFORMATIVE_GUIDELINES,
    get_available_guidelines,
    parse_checkstyle_modules,
)


def extract_readme_guideline_headers(readme_path: str) -> List[str]:
    """Extracts all '### GuidelineName' section headings from README.md.

    Args:
        readme_path: Path to the README.md file.

    Returns:
        A list of guideline names in the order they appear in README.md.

    Raises:
        FileNotFoundError: If readme_path does not exist.
    """
    if not os.path.isfile(readme_path):
        raise FileNotFoundError(f"README file not found: {readme_path}")

    headers: List[str] = []
    with open(readme_path, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(r"^###\s+([A-Za-z0-9_]+)\s*$", line.strip())
            if match:
                headers.append(match.group(1))

    return headers


def extract_readme_toc_guidelines(readme_path: str) -> List[str]:
    """Extracts guideline entries from the Table of Contents in README.md.

    Args:
        readme_path: Path to the README.md file.

    Returns:
        A list of guideline names listed in the Table of Contents.

    Raises:
        FileNotFoundError: If readme_path does not exist.
    """
    if not os.path.isfile(readme_path):
        raise FileNotFoundError(f"README file not found: {readme_path}")

    toc_entries: List[str] = []
    in_specific_guidelines = False

    with open(readme_path, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if stripped == "* [Specific Guidelines](#specific-guidelines)":
                in_specific_guidelines = True
                continue
            if in_specific_guidelines:
                if stripped.startswith("* [") and not line.startswith(" "):
                    # Hit next top-level TOC entry (e.g. * [References](#references))
                    break
                match = re.match(r"^\s+\*\s+\[([A-Za-z0-9_]+)\]\(#[a-z0-9_-]+\)\s*$", line)
                if match:
                    toc_entries.append(match.group(1))

    return toc_entries


def check_synchronization(
    repo_root: str,
) -> Tuple[bool, List[str]]:
    """Performs full sync and consistency checks across the repository.

    Args:
        repo_root: Path to the root of the cs1302-styleguide repository.

    Returns:
        A tuple of (is_valid, list_of_error_messages).
    """
    errors: List[str] = []

    xml_path = os.path.join(repo_root, "cs1302_checks.xml")
    guidelines_dir = os.path.join(repo_root, "guidelines")
    readme_path = os.path.join(repo_root, "README.md")

    # 1. Parse XML modules
    try:
        xml_modules: Set[str] = set(parse_checkstyle_modules(xml_path))
    except Exception as exc:  # pylint: disable=broad-except
        errors.append(f"Failed to parse XML checks file '{xml_path}': {exc}")
        return False, errors

    # 2. Get available guidelines
    try:
        guidelines_map = get_available_guidelines(guidelines_dir)
        guideline_files: Set[str] = set(guidelines_map.keys())
    except Exception as exc:  # pylint: disable=broad-except
        errors.append(f"Failed to read guidelines directory '{guidelines_dir}': {exc}")
        return False, errors

    # 3. Check parity between XML and guidelines/
    expected_guidelines = xml_modules | INFORMATIVE_GUIDELINES
    missing_in_guidelines = expected_guidelines - guideline_files
    if missing_in_guidelines:
        errors.append(
            f"Active XML modules missing from guidelines/ directory: {', '.join(sorted(missing_in_guidelines))}"
        )

    extra_in_guidelines = guideline_files - expected_guidelines
    if extra_in_guidelines:
        errors.append(
            f"Extra files in guidelines/ directory not in XML or informative set: {', '.join(sorted(extra_in_guidelines))}"
        )

    # 4. Check README.md section headers
    try:
        readme_headers = extract_readme_guideline_headers(readme_path)
    except Exception as exc:  # pylint: disable=broad-except
        errors.append(f"Failed to read README.md: {exc}")
        return False, errors

    headers_set = set(readme_headers)
    missing_in_readme = guideline_files - headers_set
    if missing_in_readme:
        errors.append(
            f"Guidelines missing from README.md section headers: {', '.join(sorted(missing_in_readme))}"
        )

    extra_in_readme = headers_set - guideline_files
    if extra_in_readme:
        errors.append(
            f"README.md contains headers not in guidelines/: {', '.join(sorted(extra_in_readme))}"
        )

    # 5. Check alphabetical ordering in README.md sections
    if readme_headers != sorted(readme_headers):
        errors.append("Guideline sections in README.md are not in alphabetical order.")

    # 6. Check Table of Contents
    try:
        toc_entries = extract_readme_toc_guidelines(readme_path)
    except Exception as exc:  # pylint: disable=broad-except
        errors.append(f"Failed to extract TOC from README.md: {exc}")
        return False, errors

    toc_set = set(toc_entries)
    missing_in_toc = guideline_files - toc_set
    if missing_in_toc:
        errors.append(
            f"Guidelines missing from README.md Table of Contents: {', '.join(sorted(missing_in_toc))}"
        )

    if toc_entries != sorted(toc_entries):
        errors.append("Table of Contents guideline entries in README.md are not in alphabetical order.")

    is_valid = len(errors) == 0
    return is_valid, errors


def main(argv: Optional[List[str]] = None) -> int:
    """Main CLI entry point for check_sync.py.

    Args:
        argv: Command-line arguments (defaults to sys.argv[1:]).

    Returns:
        0 if all synchronization checks pass, 1 otherwise.
    """
    parser = argparse.ArgumentParser(
        description="Verify synchronization between cs1302_checks.xml, guidelines/, and README.md."
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Path to repository root (default: current directory).",
    )

    args = parser.parse_args(argv)

    is_valid, errors = check_synchronization(args.repo_root)

    if is_valid:
        print("✓ Synchronization check passed: cs1302_checks.xml, guidelines/, and README.md are 100% in sync.")
        return 0

    print("✗ Synchronization check failed with the following errors:", file=sys.stderr)
    for err in errors:
        print(f"  - {err}", file=sys.stderr)

    return 1


if __name__ == "__main__":
    sys.exit(main())
