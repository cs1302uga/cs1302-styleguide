#!/bin/bash
# ==============================================================================
# Script: install.sh
# Description: Installs CSCI 1302 style guide resources, including style check
#              definitions (XML), Checkstyle binaries, and course wrapper scripts.
#              Supports both local execution and remote curl-piped execution.
#
# Normative References:
#   1. IEEE Std 1003.1-2017 (POSIX.1), Shell Command Language
#      https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html
#   2. Filesystem Hierarchy Standard (FHS) v3.0: /usr/local & /share
#      https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch04s09.html
#
# Informative References:
#   1. CSCI 1302 Code Style Guide
#      https://github.com/cs1302uga/cs1302-styleguide
#   2. Checkstyle Configuration Documentation
#      https://checkstyle.sourceforge.io/config.html
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
VERBOSE=false
DRY_RUN=false
PASSTHROUGH_ARGS=()

# Determine script location if executed from local filesystem
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

Install CSCI ${COURSE_NUM} Code Style Guide checks, Checkstyle, and wrapper scripts.

Options:
  -p, --prefix=PATH       Installation prefix directory
                          (default: ${DEFAULT_SYSTEM_PREFIX} if writable, else ${DEFAULT_USER_PREFIX})
  -v, --version=VERSION   Checkstyle version to install (e.g., 10.21.4 or 'latest')
                          (default: latest)
  -c, --course=NUM        Course number (default: ${COURSE_NUM})
      --guide-url=URL     URL to course style guide (default: ${GUIDE_URL})
  -f, --force             Force re-installation if directories/files already exist
      --verbose           Show detailed execution output
  -n, --dry-run           Display actions that would be taken without modifying filesystem
  -h, --help              Show this help message and exit

Remote Installation Example:
  /bin/bash -c "\$(curl -fsSL ${RAW_REPO_BASE}/install.sh)"
EOF
}

# ------------------------------------------------------------------------------
# Asset Retrieval & Remote Fallback
# ------------------------------------------------------------------------------

# Download or copy an asset to a destination file path
# Arguments:
#   $1: Relative asset path in repo (e.g. "cs1302_checks.xml")
#   $2: Target destination file path
function install_asset {
    local rel_path="$1"
    local dest_file="$2"
    local local_src="${SCRIPT_DIR}/${rel_path}"

    if [[ -n "${SCRIPT_DIR}" && -f "${local_src}" ]]; then
        log_verbose "Copying local asset: ${local_src} -> ${dest_file}"
        run_cmd cp "${local_src}" "${dest_file}"
    else
        local remote_url="${RAW_REPO_BASE}/${rel_path}"
        log_verbose "Fetching remote asset: ${remote_url} -> ${dest_file}"
        if [[ "${DRY_RUN}" == true ]]; then
            echo "[dry-run] Download ${remote_url} -> ${dest_file}"
        else
            if command -v curl >/dev/null 2>&1; then
                curl -fsSL -o "${dest_file}" "${remote_url}"
            elif command -v wget >/dev/null 2>&1; then
                wget -q -O "${dest_file}" "${remote_url}"
            else
                log_error "Neither curl nor wget is available to fetch remote asset: ${remote_url}"
                return 1
            fi
        fi
    fi
}

# ------------------------------------------------------------------------------
# CLI Argument Parsing
# ------------------------------------------------------------------------------

while [[ $# -gt 0 ]]; do
    case "$1" in
        -p|--prefix)
            PREFIX="$2"
            PASSTHROUGH_ARGS+=("--prefix=$2")
            shift 2
            ;;
        --prefix=*)
            PREFIX="${1#*=}"
            PASSTHROUGH_ARGS+=("$1")
            shift 1
            ;;
        -v|--version)
            TARGET_VERSION="$2"
            PASSTHROUGH_ARGS+=("--version=$2")
            shift 2
            ;;
        --version=*)
            TARGET_VERSION="${1#*=}"
            PASSTHROUGH_ARGS+=("$1")
            shift 1
            ;;
        -c|--course)
            COURSE_NUM="$2"
            PASSTHROUGH_ARGS+=("--course=$2")
            shift 2
            ;;
        --course=*)
            COURSE_NUM="${1#*=}"
            PASSTHROUGH_ARGS+=("$1")
            shift 1
            ;;
        --guide-url=*)
            GUIDE_URL="${1#*=}"
            PASSTHROUGH_ARGS+=("$1")
            shift 1
            ;;
        -f|--force)
            PASSTHROUGH_ARGS+=("--force")
            shift 1
            ;;
        --verbose)
            VERBOSE=true
            PASSTHROUGH_ARGS+=("--verbose")
            shift 1
            ;;
        -n|--dry-run)
            DRY_RUN=true
            PASSTHROUGH_ARGS+=("--dry-run")
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
    PASSTHROUGH_ARGS+=("--prefix=${PREFIX}")
fi

log_info "Installing CSCI ${COURSE_NUM} Style Guide environment"
log_info "Installation prefix: ${PREFIX}"

# Verify permissions
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
# Step 1: Install Checks Configuration XML
# ------------------------------------------------------------------------------

SHARE_DIR="${PREFIX}/share"
CHECKS_XML_DEST="${SHARE_DIR}/cs${COURSE_NUM}_checks.xml"
CHECKS_XML_SRC="cs${COURSE_NUM}_checks.xml"

log_info "Installing style checks XML to '${CHECKS_XML_DEST}'..."
run_cmd mkdir -p "${SHARE_DIR}"
install_asset "${CHECKS_XML_SRC}" "${CHECKS_XML_DEST}"

# ------------------------------------------------------------------------------
# Step 2: Delegate to upgrade.sh for Checkstyle Download & Script Generation
# ------------------------------------------------------------------------------

TEMP_UPGRADE_DIR=""
UPGRADE_EXEC=""

if [[ -n "${SCRIPT_DIR}" && -f "${SCRIPT_DIR}/upgrade.sh" ]]; then
    UPGRADE_EXEC="${SCRIPT_DIR}/upgrade.sh"
else
    # Fetch upgrade.sh into temporary directory for remote execution
    TEMP_UPGRADE_DIR="$(mktemp -d)"
    trap 'rm -rf "${TEMP_UPGRADE_DIR}"' EXIT
    UPGRADE_EXEC="${TEMP_UPGRADE_DIR}/upgrade.sh"
    install_asset "upgrade.sh" "${UPGRADE_EXEC}"
    if [[ "${DRY_RUN}" == false ]]; then
        chmod +x "${UPGRADE_EXEC}"
    fi
fi

log_info "Running upgrade workflow to download Checkstyle (${TARGET_VERSION})..."
if [[ "${DRY_RUN}" == true ]]; then
    echo "[dry-run] ${UPGRADE_EXEC} ${PASSTHROUGH_ARGS[*]}"
else
    "${UPGRADE_EXEC}" "${PASSTHROUGH_ARGS[@]}"
fi

# ------------------------------------------------------------------------------
# Step 3: Verification & Path Guidance
# ------------------------------------------------------------------------------

BIN_DIR="${PREFIX}/bin"
MAN_DIR="${PREFIX}/share/man"

echo ""
log_info "Installation complete!"
log_info "CSCI ${COURSE_NUM} style checks installed in: ${PREFIX}"
echo ""

# Check if BIN_DIR is already in user's PATH
if [[ ":${PATH}:" != *":${BIN_DIR}:"* ]]; then
    echo "Notice: '${BIN_DIR}' is not currently in your \$PATH."
    echo "To use 'check${COURSE_NUM}' and 'checkstyle' from anywhere, add the following to your shell profile (~/.bashrc or ~/.zshrc):"
    echo ""
    echo "  export PATH=\"${BIN_DIR}:\$PATH\""
    echo ""
fi

# Check if MAN_DIR is already in user's MANPATH
CURRENT_MANPATH="${MANPATH:-}"
if [[ ":${CURRENT_MANPATH}:" != *":${MAN_DIR}:"* ]]; then
    echo "Notice: '${MAN_DIR}' is not currently in your \$MANPATH."
    echo "To view manual pages using 'man check${COURSE_NUM}', add the following to your shell profile (~/.bashrc or ~/.zshrc):"
    echo ""
    echo "  export MANPATH=\"${MAN_DIR}:\${MANPATH:-}\""
    echo ""
fi

exit 0
