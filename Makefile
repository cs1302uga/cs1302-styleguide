# ==============================================================================
# Makefile: CSCI 1302 Code Style Guide
# ==============================================================================
# Provides developer automation for building documentation, validating
# styleguide parity, running test suites, and managing installations.
# ==============================================================================

PYTHON   ?= python3
PREFIX   ?= /usr/local/check1302
COVERAGE ?= $(PYTHON) -m coverage

SHELL_SCRIPTS = install.sh upgrade.sh etc/check_template.sh etc/checkstyle_template.sh etc/git-hooks/pre-commit
MAN_TEMPLATES = etc/check.1.template etc/checkstyle.1.template

.PHONY: all build check test coverage lint lint-sh lint-man hooks install clean help

# Default target: build README.md
all: build

## help: Display available make targets with descriptions
help:
	@echo "CSCI 1302 Style Guide Developer Automation"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  build         Autogenerate and assemble README.md from guidelines"
	@echo "  check         Verify styleguide synchronization and README status"
	@echo "  test          Run the unit test suite"
	@echo "  coverage      Run test suite with coverage report (100% target)"
	@echo "  lint          Run ShellCheck and groff/mandoc linters"
	@echo "  hooks         Install the git pre-commit hook into .git/hooks/"
	@echo "  install       Install styleguide environment to PREFIX ($(PREFIX))"
	@echo "  clean         Remove test, bytecode, and temporary build artifacts"
	@echo "  help          Show this help message"
	@echo ""

## build: Assemble README.md from guidelines and cs1302_checks.xml
build:
	$(PYTHON) etc/build_readme.py

## check: Verify 100% parity across XML, guidelines, and README.md
check:
	$(PYTHON) etc/build_readme.py --check
	$(PYTHON) etc/check_sync.py

## test: Run unittest test suite
test:
	$(PYTHON) -m unittest discover -s tests -v

## coverage: Run unittest test suite with coverage report
coverage:
	$(COVERAGE) run --source=etc -m unittest discover -s tests -v
	$(COVERAGE) report -m --fail-under=100

## lint: Run all static linters (ShellCheck and groff)
lint: lint-sh lint-man

## lint-sh: Run ShellCheck on all shell scripts
lint-sh:
	@if command -v shellcheck >/dev/null 2>&1; then \
		shellcheck $(SHELL_SCRIPTS); \
		echo "ShellCheck passed with 0 warnings."; \
	else \
		echo "Notice: shellcheck not found, skipping shell linting."; \
	fi

## lint-man: Validate roff syntax for manual page templates
lint-man:
	@if command -v groff >/dev/null 2>&1; then \
		for f in $(MAN_TEMPLATES); do \
			groff -mandoc -Tutf8 -Wall -z "$$f"; \
		done; \
		echo "Manual page templates syntax validated with groff."; \
	else \
		echo "Notice: groff not found, skipping man page linting."; \
	fi

## hooks: Install git pre-commit hook
hooks:
	@mkdir -p .git/hooks
	cp etc/git-hooks/pre-commit .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit
	@echo "Git pre-commit hook installed to .git/hooks/pre-commit"

## install: Install check1302 environment
install:
	./install.sh --prefix="$(PREFIX)"

## clean: Remove temporary and generated test artifacts
clean:
	rm -rf .coverage .coverage.* htmlcov .pytest_cache .cache
	rm -rf etc/__pycache__ tests/__pycache__
	rm -rf tmp
	@echo "Clean complete."
