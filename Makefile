# ==============================================================================
# Makefile: CSCI 1302 Code Style Guide
# ==============================================================================
# Provides developer automation for building documentation, validating
# styleguide parity, running test suites, and managing installations.
# ==============================================================================

# Executables & CLI Tools
PYTHON            ?= python3
COVERAGE          ?= $(PYTHON) -m coverage
SHELLCHECK        ?= shellcheck
GROFF             ?= groff
CURL              ?= curl
TAR               ?= tar

# Installation & Verification Settings
PREFIX            ?= /usr/local/check1302
INSTALL_SCRIPT    ?= ./install.sh
BUILD_README_PY   ?= etc/build_readme.py
CHECK_SYNC_PY     ?= etc/check_sync.py
TEST_DIR          ?= tests
COVERAGE_SOURCE   ?= etc
COVERAGE_MIN      ?= 100
GIT_HOOK_SRC      ?= etc/git-hooks/pre-commit
GIT_HOOK_DST      ?= .git/hooks/pre-commit

# Host OS & Architecture Detection
UNAME_S           ?= $(shell uname -s)
UNAME_M           ?= $(shell uname -m)

ifeq ($(UNAME_S),Darwin)
    ADOPT_OS      ?= mac
else
    ADOPT_OS      ?= linux
endif

ifneq (,$(filter $(UNAME_M),x86_64 amd64 x64))
    ADOPT_ARCH    ?= x64
else ifneq (,$(filter $(UNAME_M),arm64 aarch64))
    ADOPT_ARCH    ?= aarch64
else
    ADOPT_ARCH    ?= $(UNAME_M)
endif

# Java Multi-Version Testing & Temurin Cache
JAVA_VERSIONS     ?= 21 25
CACHE_DIR         ?= .cache
JDK_CACHE         ?= $(CACHE_DIR)/temurin/$(ADOPT_OS)-$(ADOPT_ARCH)
ADOPTIUM_API_URL  ?= https://api.adoptium.net/v3/binary/latest
ADOPTIUM_TIMEOUT  ?= 3

# File & Directory Sets
SHELL_SCRIPTS     = install.sh upgrade.sh etc/check_template.sh etc/checkstyle_template.sh etc/git-hooks/pre-commit
MAN_TEMPLATES     = etc/check.1.template etc/checkstyle.1.template
CLEAN_DIRS        = .coverage .coverage.* htmlcov .pytest_cache $(CACHE_DIR)/style_conformance_cache.json etc/__pycache__ $(TEST_DIR)/__pycache__ tmp

.PHONY: all build check test test-all-java setup-all-java upgrade-all-java ci coverage lint lint-sh lint-man hooks install clean clean-all help

# Default target: build README.md
all: build

## help: Display available make targets with descriptions
help:
	@echo "CSCI 1302 Style Guide Developer Automation"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  build            Autogenerate and assemble README.md from guidelines"
	@echo "  check            Verify styleguide synchronization and README status"
	@echo "  test             Run the unit test suite with cached Temurin $(JAVA_VERSIONS)"
	@echo "  setup-all-java   Download and cache Temurin $(JAVA_VERSIONS) (auto-updates)"
	@echo "  upgrade-all-java Force check and upgrade cached Temurin JDKs"
	@echo "  ci               Run all CI checks locally (lint, check, test-all-java)"
	@echo "  coverage         Run test suite with coverage report ($(COVERAGE_MIN)% target)"
	@echo "  lint             Run ShellCheck and groff/mandoc linters"
	@echo "  hooks            Install the git pre-commit hook into $(GIT_HOOK_DST)"
	@echo "  install          Install styleguide environment to PREFIX ($(PREFIX))"
	@echo "  clean            Remove test, bytecode, and temporary build artifacts"
	@echo "  clean-all        Remove all build artifacts and cached JDK downloads"
	@echo "  help             Show this help message"
	@echo ""

## build: Assemble README.md from guidelines and cs1302_checks.xml
build:
	$(PYTHON) $(BUILD_README_PY)

## check: Verify 100% parity across XML, guidelines, and README.md
check:
	$(PYTHON) $(BUILD_README_PY) --check
	$(PYTHON) $(CHECK_SYNC_PY)

## test: Run unittest test suite
test: ci

## setup-all-java: Download and cache Eclipse Temurin JDKs (auto-updates with offline fallback)
setup-all-java:
	@mkdir -p $(JDK_CACHE); \
	for ver in $(JAVA_VERSIONS); do \
		CACHED_JAVA=""; \
		if [ -x "$(JDK_CACHE)/$$ver/Contents/Home/bin/java" ]; then \
			CACHED_JAVA="$(JDK_CACHE)/$$ver/Contents/Home/bin/java"; \
		elif [ -x "$(JDK_CACHE)/$$ver/bin/java" ]; then \
			CACHED_JAVA="$(JDK_CACHE)/$$ver/bin/java"; \
		fi; \
		CACHED_URL=""; \
		[ -f "$(JDK_CACHE)/$$ver/.release_url" ] && CACHED_URL="$$(cat "$(JDK_CACHE)/$$ver/.release_url" 2>/dev/null)"; \
		REMOTE_URL="$$($(CURL) -sIL --max-time $(ADOPTIUM_TIMEOUT) "$(ADOPTIUM_API_URL)/$$ver/ga/$(ADOPT_OS)/$(ADOPT_ARCH)/jdk/hotspot/normal/eclipse" 2>/dev/null | grep -iE '^location:' | head -n 1 | tr -d '\r' | awk '{print $$2}')"; \
		if [ -n "$$REMOTE_URL" ]; then \
			if [ -n "$$CACHED_JAVA" ] && [ -n "$$CACHED_URL" ] && [ "$$REMOTE_URL" = "$$CACHED_URL" ]; then \
				echo "[OK] Temurin $$ver ($(ADOPT_OS)/$(ADOPT_ARCH)) is up to date: $$("$$CACHED_JAVA" -version 2>&1 | head -n 1)"; \
			else \
				echo "==> Downloading/Updating Eclipse Temurin $$ver ($(ADOPT_OS)/$(ADOPT_ARCH))..."; \
				rm -rf "$(JDK_CACHE)/$$ver"; \
				mkdir -p "$(JDK_CACHE)/$$ver"; \
				$(CURL) -fsSL "$$REMOTE_URL" | $(TAR) -xz -C "$(JDK_CACHE)/$$ver" --strip-components=1 || { echo "Error downloading Temurin $$ver" >&2; exit 1; }; \
				echo "$$REMOTE_URL" > "$(JDK_CACHE)/$$ver/.release_url"; \
			fi; \
		else \
			if [ -n "$$CACHED_JAVA" ]; then \
				echo "[OK] Temurin $$ver ($(ADOPT_OS)/$(ADOPT_ARCH)) already cached (offline mode): $$("$$CACHED_JAVA" -version 2>&1 | head -n 1)"; \
			else \
				echo "Error: Java $$ver is not cached and could not be fetched from Adoptium (network unavailable)." >&2; \
				exit 1; \
			fi; \
		fi; \
	done

## upgrade-all-java: Force check and upgrade of cached Temurin JDKs
upgrade-all-java: setup-all-java

## test-all-java: Run unit tests across cached Temurin JDKs
test-all-java: setup-all-java
	@for ver in $(JAVA_VERSIONS); do \
		JH=""; \
		if [ -d "$(JDK_CACHE)/$$ver/Contents/Home" ]; then \
			JH="$(CURDIR)/$(JDK_CACHE)/$$ver/Contents/Home"; \
		elif [ -d "$(JDK_CACHE)/$$ver" ] && [ -x "$(JDK_CACHE)/$$ver/bin/java" ]; then \
			JH="$(CURDIR)/$(JDK_CACHE)/$$ver"; \
		fi; \
		if [ -n "$$JH" ] && [ -d "$$JH" ]; then \
			echo "================================================================================"; \
			echo " Running test suite with Temurin $$ver ($$JH)"; \
			echo "================================================================================"; \
			PATH="$$JH/bin:$$PATH" JAVA_HOME="$$JH" "$$JH/bin/java" -version; \
			PATH="$$JH/bin:$$PATH" JAVA_HOME="$$JH" "$$JH/bin/javac" -version; \
			PATH="$$JH/bin:$$PATH" JAVA_HOME="$$JH" $(PYTHON) -m unittest discover -s $(TEST_DIR) -v || exit 1; \
		else \
			echo "Error: Java $$ver not found in $(JDK_CACHE)/$$ver. Run 'make setup-all-java'." >&2; \
			exit 1; \
		fi; \
	done

## ci: Run all local CI verification checks (lint, check, test across Java versions)
ci: lint check test-all-java

## coverage: Run unittest test suite with coverage report
coverage:
	$(COVERAGE) run --source=$(COVERAGE_SOURCE) -m unittest discover -s $(TEST_DIR) -v
	$(COVERAGE) report -m --fail-under=$(COVERAGE_MIN)

## lint: Run all static linters (ShellCheck and groff)
lint: lint-sh lint-man

## lint-sh: Run ShellCheck on all shell scripts
lint-sh:
	@if command -v $(SHELLCHECK) >/dev/null 2>&1; then \
		$(SHELLCHECK) $(SHELL_SCRIPTS); \
		echo "ShellCheck passed with 0 warnings."; \
	else \
		echo "Notice: $(SHELLCHECK) not found, skipping shell linting."; \
	fi

## lint-man: Validate roff syntax for manual page templates
lint-man:
	@if command -v $(GROFF) >/dev/null 2>&1; then \
		for f in $(MAN_TEMPLATES); do \
			$(GROFF) -mandoc -Tutf8 -Wall -z "$$f"; \
		done; \
		echo "Manual page templates syntax validated with $(GROFF)."; \
	else \
		echo "Notice: $(GROFF) not found, skipping man page linting."; \
	fi

## hooks: Install git pre-commit hook
hooks:
	@mkdir -p $(dir $(GIT_HOOK_DST))
	cp $(GIT_HOOK_SRC) $(GIT_HOOK_DST)
	chmod +x $(GIT_HOOK_DST)
	@echo "Git pre-commit hook installed to $(GIT_HOOK_DST)"

## install: Install check1302 environment
install:
	$(INSTALL_SCRIPT) --prefix="$(PREFIX)"

## clean: Remove temporary and generated test artifacts
clean:
	rm -rf $(CLEAN_DIRS)
	@echo "Clean complete."

## clean-all: Clean all build artifacts, test caches, and cached JDKs
clean-all: clean
	rm -rf $(CACHE_DIR)
	@echo "Clean-all complete (including cached JDKs)."
