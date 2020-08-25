

test:
	@python3 -m pytest -s

example:
	@python3 ./examples/ufa.py
	@python3 ./examples/fna.py
	@python3 ./examples/pna.py
	@python3 ./examples/ena.py

install:
	@pip install .

clean:
	rm -rf logs cache .pytest_cache