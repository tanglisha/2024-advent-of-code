sources = advent_of_code

.PHONY: test format lint unittest pre-commit clean
test: format lint unittest

format:
	isort $(sources)
	black $(sources)

lint:
	flake8 $(sources)
	mypy $(sources)

unittest:
	pytest

pre-commit:
	pre-commit run --all-files

clean:
	rm -rf .mypy_cache .pytest_cache
	rm -rf *.egg-info
	rm -rf .tox dist site
	rm -rf coverage.xml .coverage
