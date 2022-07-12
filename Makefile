.PHONY: coverage install_deps format lint publish push test tox

coverage:  ## Run tests with coverage
	python -m coverage erase
	python -m coverage run --include=calculator/* -m pytest -ra \
	                       --doctest-modules --doctest-continue-on-failure
	python -m coverage report -m
	python -m coverage xml

install_deps:  ## Install dependencies
	python -m pip install --upgrade pip
	python -m pip install black mccabe flake8 flit pyflakes mypy pylint \
	                      hypothesis pytest coverage tox tox-gh-actions 

format:  ## Format code
	python -m black calculator
	python -m black tests

lint:  ## Lint and static-check
	python -m flake8 calculator
	python -m pyflakes -V calculator
	python -m mypy calculator
	python -m pylint --verbose calculator

publish:  ## Publish to PyPi
	python -m flit publish

push:  ## Push code with tags
	git push && git push --tags

test:  ## Run tests
	python -m pytest -ra --doctest-modules --doctest-continue-on-failure

tox:   ## Run tox
	python -m tox
