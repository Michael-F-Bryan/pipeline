SOLVER_DIR = solver
PYTEST_ARGS = -v
PYTHON = python

tests:
	cd $(SOLVER_DIR) && $(PYTHON) -m pytest $(PYTEST_ARGS)


.PHONY: tests

