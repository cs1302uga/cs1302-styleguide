#!/bin/bash
# ==============================================================================
# Script: upgrade.sh
# Description: Downloads and upgrades Checkstyle to a target or latest release,
#              renders course-specific style checker wrappers from templates,
#              and updates installation symlinks.
#
# Normative References:
#   1. IEEE Std 1003.1-2017 (POSIX.1), Shell Command Language
#      https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html
#   2. Filesystem Hierarchy Standard (FHS) v3.0: /usr/local & /share
#      https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch04s09.html
#   3. GitHub REST API: Releases
#      https://docs.github.com/en/rest/releases/releases
#   4. Checkstyle Release Packaging
#      https://github.com/checkstyle/checkstyle/releases
#
# Informative References:
#   1. CSCI 1302 Code Style Guide
#      https://github.com/cs1302uga/cs1302-styleguide
# ==============================================================================
# Local Variables:
# mode: sh
# End:

set -euo pipefail

# ------------------------------------------------------------------------------
# Default Configuration
# ------------------------------------------------------------------------------
COURSE_NUM="1302"
GUIDE_URL="https://git.io/Jm9uP"
DEFAULT_SYSTEM_PREFIX="/usr/local/check1302"
DEFAULT_USER_PREFIX="${HOME}/.local/check1302"
RAW_REPO_BASE="${CS1302_RAW_REPO:-https://raw.githubusercontent.com/cs1302uga/cs1302-styleguide/master}"

PREFIX=""
TARGET_VERSION="latest"
FORCE=false
VERBOSE=false
DRY_RUN=false
CHECKS_FILE_PATH=""

# Determine script location (if executed from local file)
SCRIPT_DIR=""
if [[ -n "${BASH_SOURCE[0]:-}" && -f "${BASH_SOURCE[0]}" ]]; then
    SCRIPT_DIR="$(cd "$(dirname "$(realpath "${BASH_SOURCE[0]}")")" && pwd)"
fi

# ------------------------------------------------------------------------------
# Logging & Helper Functions
# ------------------------------------------------------------------------------

function log_info {
    echo "==> $*" >&2
}

function log_verbose {
    if [[ "${VERBOSE}" == true ]]; then
        echo "    [verbose] $*" >&2
    fi
}

function log_error {
    echo "Error: $*" >&2
}

# Execute or display command depending on DRY_RUN mode
function run_cmd {
    if [[ "${DRY_RUN}" == true ]]; then
        echo "[dry-run] $*"
    else
        log_verbose "Executing: $*"
        "$@"
    fi
}

function print_usage {
    cat <<EOF
Usage: $(basename "$0") [OPTIONS]

Download and upgrade Checkstyle release for CSCI ${COURSE_NUM}.

Options:
  -p, --prefix=PATH       Installation prefix directory
                          (default: ${DEFAULT_SYSTEM_PREFIX} if writable, else ${DEFAULT_USER_PREFIX})
  -v, --version=VERSION   Specific Checkstyle version to install (e.g., 10.21.4 or 'latest')
                          (default: latest)
  -c, --course=NUM        Course number (default: ${COURSE_NUM})
      --checks-file=PATH  Path to style checks XML file (default: \${PREFIX}/share/cs\${COURSE}_checks.xml)
      --guide-url=URL     URL to course style guide (default: ${GUIDE_URL})
  -f, --force             Force re-installation if version directory already exists
      --verbose           Show detailed execution output
  -n, --dry-run           Display actions that would be taken without modifying filesystem
  -h, --help              Show this help message and exit

Examples:
  $(basename "$0")
  $(basename "$0") --prefix=/usr/local/cs1302 --verbose
  $(basename "$0") --version=10.21.4 --dry-run
EOF
}

# ------------------------------------------------------------------------------
# Asset Retrieval & Remote Fallback
# ------------------------------------------------------------------------------

# Retrieve content of a local or remote asset to standard output
# Arguments:
#   $1: Relative asset path (e.g., "etc/check_template.sh")
function fetch_asset_content {
    local rel_path="$1"
    local local_file="${SCRIPT_DIR}/${rel_path}"

    if [[ -n "${SCRIPT_DIR}" && -f "${local_file}" ]]; then
        log_verbose "Reading local asset: ${local_file}"
        cat "${local_file}"
    else
        local remote_url="${RAW_REPO_BASE}/${rel_path}"
        log_verbose "Fetching remote asset from: ${remote_url}"
        if command -v curl >/dev/null 2>&1; then
            curl -fsSL "${remote_url}"
        elif command -v wget >/dev/null 2>&1; then
            wget -qO- "${remote_url}"
        else
            log_error "Neither curl nor wget is available to fetch remote asset: ${remote_url}"
            return 1
        fi
    fi
}

# Fetch the download URL for the latest Checkstyle release
function fetch_latest_release_url {
    local api_url="https://api.github.com/repos/checkstyle/checkstyle/releases/latest"
    local download_url=""

    log_verbose "Querying GitHub API for latest release: ${api_url}"

    if command -v curl >/dev/null 2>&1; then
        download_url="$(curl -fsSL "${api_url}" 2>/dev/null \
            | grep -E '"browser_download_url":' \
            | grep -E 'checkstyle-[0-9.]+.*-all\.jar"' \
            | head -n 1 \
            | sed -E 's/.*"browser_download_url": *"([^"]+)".*/\1/' || true)"
    elif command -v wget >/dev/null 2>&1; then
        download_url="$(wget -qO- "${api_url}" 2>/dev/null \
            | grep -E '"browser_download_url":' \
            | grep -E 'checkstyle-[0-9.]+.*-all\.jar"' \
            | head -n 1 \
            | sed -E 's/.*"browser_download_url": *"([^"]+)".*/\1/' || true)"
    fi

    # Fallback to GitHub CLI if available and direct curl/wget failed
    if [[ -z "${download_url}" ]] && command -v gh >/dev/null 2>&1; then
        log_verbose "Falling back to GitHub CLI (gh api)..."
        download_url="$(gh api repos/checkstyle/checkstyle/releases/latest --jq '.assets[].browser_download_url' 2>/dev/null \
            | grep -E 'checkstyle-.*-all\.jar$' \
            | head -n 1 || true)"
    fi

    if [[ -z "${download_url}" ]]; then
        log_error "Failed to determine latest Checkstyle release URL from GitHub."
        return 1
    fi

    echo "${download_url}"
}

# ------------------------------------------------------------------------------
# CLI Argument Parsing
# ------------------------------------------------------------------------------

while [[ $# -gt 0 ]]; do
    case "$1" in
        -p|--prefix)
            PREFIX="$2"
            shift 2
            ;;
        --prefix=*)
            PREFIX="${1#*=}"
            shift 1
            ;;
        -v|--version)
            TARGET_VERSION="$2"
            shift 2
            ;;
        --version=*)
            TARGET_VERSION="${1#*=}"
            shift 1
            ;;
        -c|--course)
            COURSE_NUM="$2"
            shift 2
            ;;
        --course=*)
            COURSE_NUM="${1#*=}"
            shift 1
            ;;
        --checks-file=*)
            CHECKS_FILE_PATH="${1#*=}"
            shift 1
            ;;
        --guide-url=*)
            GUIDE_URL="${1#*=}"
            shift 1
            ;;
        -f|--force)
            FORCE=true
            shift 1
            ;;
        --verbose)
            VERBOSE=true
            shift 1
            ;;
        -n|--dry-run)
            DRY_RUN=true
            shift 1
            ;;
        -h|--help)
            print_usage
            exit 0
            ;;
        *)
            log_error "Unknown option: $1"
            print_usage >&2
            exit 1
            ;;
    esac
done

# ------------------------------------------------------------------------------
# Prefix Resolution & Permissions Validation
# ------------------------------------------------------------------------------

if [[ -z "${PREFIX}" ]]; then
    if [[ -w "/usr/local" || ("${EUID}" -eq 0) ]]; then
        PREFIX="${DEFAULT_SYSTEM_PREFIX}"
    else
        PREFIX="${DEFAULT_USER_PREFIX}"
    fi
fi

if [[ -z "${CHECKS_FILE_PATH}" ]]; then
    CHECKS_FILE_PATH="${PREFIX}/share/cs${COURSE_NUM}_checks.xml"
fi

log_info "Target prefix: ${PREFIX}"
log_verbose "Style checks path: ${CHECKS_FILE_PATH}"

# Check write permissions unless in dry-run mode
if [[ "${DRY_RUN}" == false ]]; then
    target_check_dir="${PREFIX}"
    while [[ ! -d "${target_check_dir}" && "${target_check_dir}" != "/" ]]; do
        target_check_dir="$(dirname "${target_check_dir}")"
    done
    if [[ ! -w "${target_check_dir}" ]]; then
        log_error "Cannot write to '${PREFIX}' (insufficient permissions)."
        log_error "Please re-run with sudo or specify a user directory (e.g., --prefix=${DEFAULT_USER_PREFIX})."
        exit 1
    fi
fi

# ------------------------------------------------------------------------------
# Release Resolution & Download
# ------------------------------------------------------------------------------

RELEASE_URL=""
if [[ "${TARGET_VERSION}" == "latest" ]]; then
    log_info "Resolving latest Checkstyle release..."
    RELEASE_URL="$(fetch_latest_release_url)"
else
    RELEASE_URL="https://github.com/checkstyle/checkstyle/releases/download/checkstyle-${TARGET_VERSION}/checkstyle-${TARGET_VERSION}-all.jar"
fi

FILENAME="$(basename "${RELEASE_URL}")"
RELEASE_DIR_NAME="${FILENAME%-all.jar}"
RELEASE_DIR_NAME="${RELEASE_DIR_NAME%.jar}"
VERSION_NUM="${RELEASE_DIR_NAME#checkstyle-}"

log_info "Checkstyle version to install: ${VERSION_NUM}"
log_verbose "Download URL: ${RELEASE_URL}"

VERSION_DIR="${PREFIX}/${RELEASE_DIR_NAME}"
CHECKSTYLE_JAR="${VERSION_DIR}/checkstyle.jar"

if [[ -d "${VERSION_DIR}" && "${FORCE}" == false ]]; then
    log_info "${RELEASE_DIR_NAME} is already installed in '${VERSION_DIR}'."
    log_info "Updating symlinks (use --force to re-download)..."
else
    log_info "Installing ${RELEASE_DIR_NAME} to '${VERSION_DIR}'..."

    run_cmd mkdir -p "${VERSION_DIR}"

    # Download Checkstyle JAR
    log_info "Downloading Checkstyle JAR..."
    if [[ "${DRY_RUN}" == true ]]; then
        echo "[dry-run] Download ${RELEASE_URL} -> ${CHECKSTYLE_JAR}"
    else
        if command -v curl >/dev/null 2>&1; then
            curl -fsSL -o "${CHECKSTYLE_JAR}" "${RELEASE_URL}"
        elif command -v wget >/dev/null 2>&1; then
            wget -q -O "${CHECKSTYLE_JAR}" "${RELEASE_URL}"
        fi
    fi
fi

# ------------------------------------------------------------------------------
# Template Rendering & Script Generation
# ------------------------------------------------------------------------------

CHECK_SCRIPT="${VERSION_DIR}/check${COURSE_NUM}"
CHECKSTYLE_SCRIPT="${VERSION_DIR}/checkstyle"
VERSION_MAN_DIR="${VERSION_DIR}/share/man/man1"
CHECK_MAN="${VERSION_MAN_DIR}/check${COURSE_NUM}.1"
CHECKSTYLE_MAN="${VERSION_MAN_DIR}/checkstyle.1"

log_info "Generating wrapper scripts and manual pages from templates..."

# Render check<COURSE> wrapper
if [[ "${DRY_RUN}" == true ]]; then
    echo "[dry-run] Render check_template.sh -> ${CHECK_SCRIPT}"
else
    fetch_asset_content "etc/check_template.sh" \
        | sed \
            -e "s|@COURSE_NUM@|${COURSE_NUM}|g" \
            -e "s|@GUIDE_URL@|${GUIDE_URL}|g" \
            -e "s|@CHECKS_FILE_PATH@|${CHECKS_FILE_PATH}|g" \
        > "${CHECK_SCRIPT}"
    chmod +x "${CHECK_SCRIPT}"
fi

# Render checkstyle wrapper
if [[ "${DRY_RUN}" == true ]]; then
    echo "[dry-run] Render checkstyle_template.sh -> ${CHECKSTYLE_SCRIPT}"
else
    fetch_asset_content "etc/checkstyle_template.sh" > "${CHECKSTYLE_SCRIPT}"
    chmod +x "${CHECKSTYLE_SCRIPT}"
fi

# Render manual pages
if [[ "${DRY_RUN}" == true ]]; then
    echo "[dry-run] mkdir -p ${VERSION_MAN_DIR}"
    echo "[dry-run] Render check.1.template -> ${CHECK_MAN}"
    echo "[dry-run] Render checkstyle.1.template -> ${CHECKSTYLE_MAN}"
else
    mkdir -p "${VERSION_MAN_DIR}"
    fetch_asset_content "etc/check.1.template" \
        | sed \
            -e "s|@COURSE_NUM@|${COURSE_NUM}|g" \
            -e "s|@GUIDE_URL@|${GUIDE_URL}|g" \
            -e "s|@CHECKS_FILE_PATH@|${CHECKS_FILE_PATH}|g" \
        > "${CHECK_MAN}"
    fetch_asset_content "etc/checkstyle.1.template" \
        | sed \
            -e "s|@COURSE_NUM@|${COURSE_NUM}|g" \
            -e "s|@GUIDE_URL@|${GUIDE_URL}|g" \
            -e "s|@CHECKS_FILE_PATH@|${CHECKS_FILE_PATH}|g" \
        > "${CHECKSTYLE_MAN}"
fi

# ------------------------------------------------------------------------------
# Symlink Management
# ------------------------------------------------------------------------------

LATEST_SYMLINK="${PREFIX}/latest"
BIN_DIR="${PREFIX}/bin"
PREFIX_MAN_DIR="${PREFIX}/share/man/man1"

log_info "Updating 'latest' and executable/manual symlinks..."
if [[ "${DRY_RUN}" == true ]]; then
    echo "[dry-run] ln -sfn ${RELEASE_DIR_NAME} ${LATEST_SYMLINK}"
    echo "[dry-run] mkdir -p ${BIN_DIR}"
    echo "[dry-run] ln -sfn ../latest/check${COURSE_NUM} ${BIN_DIR}/check${COURSE_NUM}"
    echo "[dry-run] ln -sfn ../latest/checkstyle ${BIN_DIR}/checkstyle"
    echo "[dry-run] mkdir -p ${PREFIX_MAN_DIR}"
    echo "[dry-run] ln -sfn ../../../latest/share/man/man1/check${COURSE_NUM}.1 ${PREFIX_MAN_DIR}/check${COURSE_NUM}.1"
    echo "[dry-run] ln -sfn ../../../latest/share/man/man1/checkstyle.1 ${PREFIX_MAN_DIR}/checkstyle.1"
else
    (cd "${PREFIX}" && ln -sfn "${RELEASE_DIR_NAME}" latest)
    mkdir -p "${BIN_DIR}"
    (cd "${BIN_DIR}" && ln -sfn "../latest/check${COURSE_NUM}" "check${COURSE_NUM}")
    (cd "${BIN_DIR}" && ln -sfn "../latest/checkstyle" "checkstyle")
    mkdir -p "${PREFIX_MAN_DIR}"
    (cd "${PREFIX_MAN_DIR}" && ln -sfn "../../../latest/share/man/man1/check${COURSE_NUM}.1" "check${COURSE_NUM}.1")
    (cd "${PREFIX_MAN_DIR}" && ln -sfn "../../../latest/share/man/man1/checkstyle.1" "checkstyle.1")
fi

log_info "Checkstyle ${VERSION_NUM} successfully installed to ${PREFIX}"
log_info "Executables available in: ${BIN_DIR}"
log_info "Manual pages available in: ${PREFIX}/share/man"

exit 0
