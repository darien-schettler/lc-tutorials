.PHONY: install test lint format type-check docs clean build notebook test-coverage

# Install all dependencies via Poetry
install:
	poetry install

# Run tests using Pytest
test:
	poetry run pytest

# Lint the code using Ruff
lint:
	poetry run ruff check lc_tutorials

# Format the code using Ruff (replaces Black and isort)
format:
	poetry run ruff check lc_tutorials --fix

# Perform type-checking using Pyright
type-check:
	poetry run pyright

# Generate HTML documentation using Sphinx
docs:
	poetry run sphinx-build -b html docs/source docs/build

# Clean up build and Python cache files
clean:
	rm -rf dist build .pyright .ruff_cache *.egg-info
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "__pycache__" -exec rm -rf {} \;

# Build the Python package
build:
	poetry build

# Start Jupyter Lab
notebook:
	poetry run jupyter lab

# Run tests with coverage report
test-coverage:
	poetry run pytest --cov=lc_tutorials --cov-report=term-missing
