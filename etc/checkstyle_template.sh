#!/bin/bash
# ==============================================================================
# Script: checkstyle (Generated from etc/checkstyle_template.sh)
# Description: Wrapper around the Checkstyle executable JAR archive.
#              Intercepts Checkstyle exceptions (typically caused by uncompilable
#              or syntactically invalid Java code) and provides user-friendly
#              diagnostics in both plaintext and XML formats.
#
# Normative References:
#   1. IEEE Std 1003.1-2017 (POSIX.1), Shell Command Language
#      https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html
#   2. Checkstyle Command Line Interface (CLI) Specification
#      https://checkstyle.sourceforge.io/cmdline.html
#   3. Extensible Markup Language (XML) 1.0 (Fifth Edition), W3C Recommendation
#      https://www.w3.org/TR/xml/
#
# Informative References:
#   1. Checkstyle API Documentation: CheckstyleException
#      https://checkstyle.sourceforge.io/apidocs/com/puppycrawl/tools/checkstyle/api/CheckstyleException.html
# ==============================================================================
# Local Variables:
# mode: sh
# End:

set -o pipefail

# ------------------------------------------------------------------------------
# Environment & Path Resolution
# ------------------------------------------------------------------------------
SOURCE="$(realpath "${BASH_SOURCE[0]}")"
DIRNAME="$(dirname "${SOURCE}")"
CHECKSTYLE_JAR="${SOURCE}.jar"

# If the JAR is not co-located as <name>.jar, check inside the directory
if [[ ! -f "${CHECKSTYLE_JAR}" ]]; then
    CHECKSTYLE_JAR="${DIRNAME}/checkstyle.jar"
fi

# Extract version number from parent directory name (e.g., checkstyle-10.21.4 -> 10.21.4)
VERSION="$(basename "${DIRNAME}" | sed 's|checkstyle-||g')"

# Setup safe temporary file for capturing standard error
ERRORS="$(mktemp)"
trap 'rm -f "${ERRORS}"' EXIT

SUSPECT="Checkstyle suspects this file may not compile!"

# ------------------------------------------------------------------------------
# Verification & Execution
# ------------------------------------------------------------------------------
if [[ ! -f "${CHECKSTYLE_JAR}" ]]; then
    echo "Error: Checkstyle JAR not found at '${CHECKSTYLE_JAR}'" >&2
    exit 1
fi

# Execute the Checkstyle JAR with passed arguments
java -jar "${CHECKSTYLE_JAR}" "$@" 2>"${ERRORS}"
STATUS="${PIPESTATUS[0]}"

# ------------------------------------------------------------------------------
# Exception Interception & Diagnostic Formatting
# ------------------------------------------------------------------------------
if grep -qE "^com\.puppycrawl\.tools\.checkstyle\.api\.CheckstyleException" "${ERRORS}"; then
    # Check if XML format was requested via -f xml, -f=xml, or --format=xml
    if echo "$*" | grep -qE "\s(-f[=]?\s*xml|--format[=]?\s*xml)"; then
        cat <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<checkstyle version="${VERSION}">
<file>
<error line="1" severity="error" message="${SUSPECT}" source="na"/>
</file>
</checkstyle>
EOF
    else
        echo "${SUSPECT}" >&2
    fi
else
    # Forward original stderr if not a syntax/parse exception
    if [[ -s "${ERRORS}" ]]; then
        cat "${ERRORS}" >&2
    fi
fi

exit "${STATUS}"
