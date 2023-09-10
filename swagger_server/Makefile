PYTHON = python3
ENV = env
PYBIN = $(ENV)/bin
PIP = $(PYBIN)/pip
PYTEST = $(PYBIN)/pytest
PYRUN = $(PYBIN)/python3
FLAKE8 = $(PYBIN)/flake8 .  # TODO
DBDIR = var

.PHONY: environ
environ: $(PYBIN)/$(PYTHON) $(ENV)/.done

.PHONY: help
help:
	@echo "make                  # build everything"
	@echo "make test             # TODO: run tests"
	@echo "make flake8           # TODO: run flake8 linter"
	@echo "make run              # run API"
	@echo "make clean            # clean API and databases"


$(PIP) $(PYBIN)/$(PYTHON):
	rm -rf $(ENV)
	rm -rf ${DBDIR}
	mkdir ${DBDIR}
	virtualenv --no-download -p $(PYTHON) $(ENV)
	$(PIP) install -U pip setuptools tox

$(ENV)/.done: $(PIP) setup.py requirements-dev.txt
	$(PIP) install -r requirements-dev.txt -e .
	touch $(ENV)/.done

.PHONY: run
run: environ
	$(PYBIN)/$(PYTHON) application.py

.PHONY: test
test: environ
	$(PYTEST) tests

.PHONY: clean
clean:
	rm -rf $(ENV)
	${MAKE} clean-pycache

.PHONY: clean-pycache
clean-pycache:
	-find . -name '__pycache__' -type d -exec rm -rf "{}" +
	find . -name '.pytest_cache' -type d -exec rm -rf "{}" +
	find . -name '*.pyc' -delete
