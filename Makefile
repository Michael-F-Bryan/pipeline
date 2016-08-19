# Need to have $(DIGITAL_OCEAN_KEY) as an environment variable already!!!
DIGITAL_OCEAN_KEY ?= MY_SECRET_KEY
DOCKER_MACHINE_NAME = foo

SOLVER_DIR = solver
PYTEST_ARGS = -v
PYTHON = python


create-machine:
	docker-machine create --driver digitalocean \
		--digitalocean-access-token $(DIGITAL_OCEAN_KEY) \
		--digitalocean-image ubuntu-16-04-x64 \
		--digitalocean-size "2gb" \
		$(DOCKER_MACHINE_NAME)


tests:
	cd $(SOLVER_DIR) && $(PYTHON) -m pytest $(PYTEST_ARGS)


.PHONY: tests

