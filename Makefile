DIGITAL_OCEAN_KEY = 7b4aebde36f86ee9fbded46b623d1faf85129d82de5374f36740b60b15cb09a3
SOLVER_DIR = solver
PYTEST_ARGS = -v
PYTHON = python


tests:
	cd $(SOLVER_DIR) && $(PYTHON) -m pytest $(PYTEST_ARGS)


.PHONY: tests

