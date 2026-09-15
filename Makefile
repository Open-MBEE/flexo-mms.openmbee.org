.PHONY: install build serve help

PYTHON ?= python3
SITE_DIR ?= site

install: ## Install the site toolchain
	$(PYTHON) -m pip install -r docs-requirements.txt

build: ## Build the site, failing on a broken link
	$(PYTHON) -m mkdocs build --strict --site-dir $(SITE_DIR)

serve: ## Serve the site with live reload
	$(PYTHON) -m mkdocs serve --strict

help: ## Show this help
	@grep -E '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | awk -F ':.*## ' '{ printf "  %-10s %s\n", $$1, $$2 }'
