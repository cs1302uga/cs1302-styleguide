# `check1302` Installation & Maintenance Guide

This document describes how to install, configure, upgrade, and maintain the **CSCI 1302 Code Style Guide** environment (which provides the `check1302` command, etc.) using [`install.sh`](install.sh) and [`upgrade.sh`](upgrade.sh).

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Quick Start (Remote One-Liner)](#quick-start-remote-one-liner)
3. [Local Installation](#local-installation)
4. [Filesystem Layout](#filesystem-layout)
5. [Environment Setup (PATH & MANPATH)](#environment-setup-path--manpath)
6. [`install.sh` Reference](#installsh-reference)
7. [`upgrade.sh` Reference](#upgradesh-reference)
8. [Uninstallation](#uninstallation)

## Prerequisites

The installation and upgrade scripts adhere to **POSIX.1-2017** shell standards and require minimal system dependencies:

* **POSIX-compatible shell**: `bash` (v4.0+ recommended)
* **Java Runtime Environment**: Java 17+ (Java 21+ recommended) with `java` available on `PATH`
* **Download tool**: `curl` or `wget` (with fallback to `gh` CLI if available)
* **Core utilities**: `sed`, `grep`, `mkdir`, `chmod`, `ln`, `tar`

## Quick Start (Remote One-Liner)

To install the latest Checkstyle release, style rules (`cs1302_checks.xml`), and command wrappers without cloning the repository, execute:

### System-Wide Installation (Requires `sudo` / Root Access)

```bash
sudo /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/cs1302uga/cs1302-styleguide/master/install.sh)"
```

*Installs to `/usr/local/check1302` by default.*

### User-Level Installation (No Root Privileges Required)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/cs1302uga/cs1302-styleguide/master/install.sh)"
```

*Installs to `${HOME}/.local/check1302` by default when run without write access to `/usr/local`.*

## Local Installation

When working from a local clone of this repository:

```bash
# Clone the repository
git clone https://github.com/cs1302uga/cs1302-styleguide.git
cd cs1302-styleguide
```

```bash
# Install with default prefix (/usr/local/check1302 or ~/.local/check1302)
./install.sh
```

```bash
# Or install to a custom prefix
./install.sh --prefix=/opt/cs1302
```

## Filesystem Layout

The installation adheres to the **Filesystem Hierarchy Standard (FHS v3.0)**:

```plaintext
<PREFIX>/
├── bin/
│   ├── check1302 -> ../opt/checkstyle/bin/check1302
│   └── checkstyle1302 -> ../opt/checkstyle/bin/checkstyle1302
├── opt/
│   ├── checkstyle -> checkstyle-10.21.4/
│   └── checkstyle-10.21.4/
│       ├── bin/
│       │   ├── check1302
│       │   └── checkstyle1302
│       └── lib/
│           └── checkstyle-10.21.4-all.jar
└── share/
    ├── cs1302_checks.xml
    └── man/
        └── man1/
            ├── check1302.1
            └── checkstyle1302.1
```

* **`bin/`**: Public executables intended for user `PATH`.
* **`opt/checkstyle-<version>/`**: Version-isolated Checkstyle binaries and rendered launcher scripts.
* **`opt/checkstyle`**: Symlink pointing to the currently active Checkstyle version.
* **`share/`**: Architecture-independent shared assets (`cs1302_checks.xml` style definitions and manual pages).

## Environment Setup (PATH & MANPATH)

To make `check1302`, `checkstyle1302`, and their manual pages accessible in your shell:

### For Bash (`~/.bashrc` or `~/.bash_profile`)

```bash
export PREFIX="/usr/local/check1302" # or "${HOME}/.local/check1302"
export PATH="${PREFIX}/bin:${PATH}"
export MANPATH="${PREFIX}/share/man:${MANPATH:-$(manpath 2>/dev/null || true)}"
```

### For Zsh (`~/.zshrc`)

```zsh
export PREFIX="/usr/local/check1302" # or "${HOME}/.local/check1302"
export PATH="${PREFIX}/bin:${PATH}"
export MANPATH="${PREFIX}/share/man:${MANPATH:-}"
```

### Verifying the Setup

```bash
# Verify command is found
which check1302
```

```bash
# Check manual page
man check1302
```

## `install.sh` Reference

`install.sh` initializes the directory structure, installs style rule definitions and manual pages, and delegates binary acquisition to `upgrade.sh`.

### Usage

```bash
./install.sh [OPTIONS]
```

### Options

| Option | Description | Default |
| :--- | :--- | :--- |
| `-p, --prefix=PATH` | Installation prefix directory | `/usr/local/check1302` (if writable) or `~/.local/check1302` |
| `-v, --version=VER` | Checkstyle version to install (e.g., `10.21.4` or `latest`) | `latest` |
| `-c, --course=NUM` | Course number identifier | `1302` |
| `--guide-url=URL` | Course style guide reference URL | `https://git.io/Jm9uP` |
| `-f, --force` | Force re-installation over existing files | `false` |
| `--verbose` | Enable verbose debug logging | `false` |
| `-n, --dry-run` | Print actions without modifying the filesystem | `false` |
| `-h, --help` | Display usage information and exit | — |

### Examples

```bash
# Install to custom directory in verbose mode
./install.sh --prefix=/opt/check1302 --verbose
```

```bash
# Dry run to inspect actions before making changes
./install.sh --prefix=/usr/local/check1302 --dry-run
```

```bash
# Perform remote installation via curl
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/cs1302uga/cs1302-styleguide/master/install.sh)"
```

## `upgrade.sh` Reference

`upgrade.sh` downloads or updates the Checkstyle binary JAR, renders course wrapper scripts from templates, and updates version symlinks.

### Usage

```bash
./upgrade.sh [OPTIONS]
```

### Options

| Option | Description | Default |
| :--- | :--- | :--- |
| `-p, --prefix=PATH` | Target installation prefix | `/usr/local/check1302` (if writable) or `~/.local/check1302` |
| `-v, --version=VER` | Checkstyle release version to install (`latest` or exact tag) | `latest` |
| `-c, --course=NUM` | Course number identifier | `1302` |
| `--checks-file=PATH` | Path to `cs1302_checks.xml` file | `${PREFIX}/share/cs1302_checks.xml` |
| `--guide-url=URL` | Style guide URL substitution for wrappers | `https://git.io/Jm9uP` |
| `-f, --force` | Force re-download even if version directory exists | `false` |
| `--verbose` | Print detailed download and rendering logs | `false` |
| `-n, --dry-run` | Simulate download and symlink creation | `false` |
| `-h, --help` | Display usage information and exit | — |

### Examples

```bash
# Upgrade active Checkstyle to latest release
./upgrade.sh
```

```bash
# Install a specific Checkstyle release version
./upgrade.sh --version=10.21.4
```

```bash
# Perform remote upgrade via curl
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/cs1302uga/cs1302-styleguide/master/upgrade.sh)"
```

## Uninstallation

To completely remove the installed style guide environment, simply delete the prefix directory:

```bash
# For system-wide install
sudo rm -rf /usr/local/check1302
```

```bash
# For user-level install
rm -rf ~/.local/check1302
```

Then remove any corresponding `PATH` and `MANPATH` export lines from your shell configuration file (`~/.bashrc` or `~/.zshrc`).
