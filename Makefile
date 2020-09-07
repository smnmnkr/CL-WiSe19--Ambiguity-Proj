
# The binary to build (basename).
MODULE := automata

test:
	@python3 -m pytest -s -v

example:
	@python3 -m $(MODULE) ./examples/ufa.json
	@python3 -m $(MODULE) ./examples/fna.json
	@python3 -m $(MODULE) ./examples/pna.json
	@python3 -m $(MODULE) ./examples/ena.json

install:
	@pip install .

lint:
	@pre-commit run --all-files

clean:
	rm -rf logs cache .pytest_cache .mypy_cache
	clear
