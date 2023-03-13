venv: ## Create a Python virtual environment
	$(info Creating Python 3 virtual environment...)
	python3 -m venv ~/venv

install: ## Install Python dependencies
	$(info Installing dependencies...)
	python3 -m pip install --upgrade pip wheel &&\
		pip install -r requirements.txt

lint: ## Run the linter
	$(info Running linting...)
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --max-complexity=10 --max-line-length=127 --statistics

.PHONY: tests
tests: ## Run the unit tests
	$(info Running tests...)
	nosetests -vv --with-spec --spec-color --with-coverage --cover-package=service