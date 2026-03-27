# Build and wheel verification targets for ccacards

SHELL := /bin/bash

WHEEL_TEST_VENV := .venv-wheeltest
WHEEL_GLOB := dist/*.whl

.PHONY: help clean-dist clean-wheeltest build wheel-test wheel-test-clean

help:
	@echo "Targets:"
	@echo "  build            Build sdist and wheel into dist/"
	@echo "  wheel-test       Create isolated venv, install built wheel, run smoke checks"
	@echo "  clean-dist       Remove dist/ build artifacts"
	@echo "  clean-wheeltest  Remove wheel test virtual environment"
	@echo "  wheel-test-clean Run wheel-test and then clean test venv"

# ------------------------
# Build
# ------------------------

clean-dist:
	rm -rf dist

build: clean-dist
	uv build

# ------------------------
# Test Built Wheel
# ------------------------

clean-wheeltest:
	rm -rf $(WHEEL_TEST_VENV)

wheel-test: clean-wheeltest build
	@set -euo pipefail; \
	wheels=( $(WHEEL_GLOB) ); \
	if [ $${#wheels[@]} -ne 1 ]; then \
		echo "Expected exactly one wheel in dist/, found $${#wheels[@]}"; \
		ls -1 dist || true; \
		exit 1; \
	fi; \
	wheel="$${wheels[0]}"; \
	echo "Using wheel: $$wheel"; \
	uv venv $(WHEEL_TEST_VENV); \
	uv pip install --python $(WHEEL_TEST_VENV)/bin/python "$$wheel"; \
	$(WHEEL_TEST_VENV)/bin/python -c "import ccacards; print('ccacards version:', ccacards.__version__)"; \
	$(WHEEL_TEST_VENV)/bin/python -c "from ccacards.card import Card; c = Card(1); print('sample card:', c)"; \
	uv pip check --python $(WHEEL_TEST_VENV)/bin/python

wheel-test-clean: wheel-test clean-wheeltest
