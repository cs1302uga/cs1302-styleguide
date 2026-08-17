#!/bin/bash
# ==============================================================================
# Script: check@COURSE_NUM@ (Generated from etc/check_template.sh)
# Description: Custom Checkstyle wrapper for CSCI @COURSE_NUM@ Code Style Guide.
#              Audits Java source files for compliance and provides links
#              to the style guide upon detection of violations.
#
# Normative References:
#   1. IEEE Std 1003.1-2017 (POSIX.1), Shell Command Language
#      https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html
#   2. Checkstyle Command Line Interface (CLI) Specification
#      https://checkstyle.sourceforge.io/cmdline.html
#
# Informative References:
#   1. CSCI @COURSE_NUM@ Code Style Guide
#      @GUIDE_URL@
#   2. Google Java Style Guide
#      https://google.github.io/styleguide/javaguide.html
# ==============================================================================
# Local Variables:
# mode: sh
# End:

set -o pipefail

# ------------------------------------------------------------------------------
# Configuration Constants & Variables
# ------------------------------------------------------------------------------
COURSE_NAME="CSCI @COURSE_NUM@"
GUIDE_TITLE="${COURSE_NAME} Code Style Guide"
GUIDE_URL="@GUIDE_URL@"
DEFAULT_CHECKS_FILE="@CHECKS_FILE_PATH@"
CHECKS_ENV_VAR="CS@COURSE_NUM@_CHECKS"

# Resolve checks configuration: check environment variable, then fallback to default
CHECKS_CONFIG="${!CHECKS_ENV_VAR:-${DEFAULT_CHECKS_FILE}}"

CHECKSTYLE="$(dirname "${SOURCE}")/checkstyle"
if [[ ! -x "${CHECKSTYLE}" ]]; then
    if command -v checkstyle >/dev/null 2>&1; then
        CHECKSTYLE="$(command -v checkstyle)"
    fi
fi
PROG="$(basename "$0")"

# Terminal color and text styling
BOLD=$(tput bold 2>/dev/null || true)
NORM=$(tput sgr0 2>/dev/null || true)
RED=$(tput setaf 1 2>/dev/null || true)

# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------

# Print usage information to standard error or standard output.
function print_usage {
    cat <<EOF
${PROG} uses Checkstyle to check for ${GUIDE_TITLE} violations.
Usage: ${PROG} [CHECKSTYLE_OPTIONS] <files>...
EOF
}

# Check if a target element exists within an array of arguments.
# Arguments:
#   $1: Target string to find
#   $@: List of items to search
# Returns:
#   0 if target found, 1 otherwise
function element_of {
    local target="$1"
    shift
    for elem in "$@"; do
        if [[ "${elem}" == "${target}" ]]; then
            return 0
        fi
    done
    return 1
}

# ------------------------------------------------------------------------------
# Main Logic & Execution Flow
# ------------------------------------------------------------------------------

# Ensure at least one argument is supplied
if [[ $# -eq 0 ]]; then
    print_usage >&2
    exit 1
fi

# Disallow manual override of the style checks configuration via -c
if element_of "-c" "$@"; then
    echo "The -c Checkstyle option is not supported by ${PROG}." >&2
    exit 1
fi

# Verify the style checks configuration XML exists
if [[ ! -f "${CHECKS_CONFIG}" ]]; then
    echo "Error: Checks configuration file '${CHECKS_CONFIG}' not found." >&2
    echo "Please set \$${CHECKS_ENV_VAR} or verify the styleguide installation." >&2
    exit 1
fi

# Verify the checkstyle runner executable exists
if [[ ! -x "${CHECKSTYLE}" ]]; then
    echo "Error: Checkstyle runner executable '${CHECKSTYLE}' not found." >&2
    exit 1
fi

# Execute Checkstyle and strip verbose package namespaces from output
"${CHECKSTYLE}" -c "${CHECKS_CONFIG}" "$@" \
    | sed -E 's|com\.puppycrawl\.tools\.checkstyle\.(\w+\.)*||g'

STATUS="${PIPESTATUS[0]}"

# Handle violation reporting and optional browser navigation
if [[ "${STATUS}" -ne 0 ]]; then
    >&2 echo -n "${BOLD}${RED}"
    >&2 echo -n "Consult the ${GUIDE_TITLE} for information about how "
    >&2 echo -n "to fix each '[GuidelineName]' error in the audit.${NORM}"
    >&2 echo ""
    if [[ -n "${BROWSER:-}" && -n "${GUIDE_URL}" ]]; then
        "${BROWSER}" "${GUIDE_URL}" >/dev/null 2>&1 &
    fi
    exit "${STATUS}"
fi

exit 0
