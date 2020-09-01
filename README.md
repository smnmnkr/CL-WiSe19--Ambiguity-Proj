# automata

Simple NFA _(non deterministic finite automata)_ module to examine the different degrees of ambiguity of an automata on a given input or a given word length.

## Installation _(from source)_

```bash
# bash, powershell:
make install
```

## Usage

```bash
# options:
# configFile -> JSON : path to configuration json
# length -> INT : maximal word length to test | (optional/default: 15)

# run module:
python3 -m automata path/to/config.json -l 10

# run UFA, FNA, PNA, ENA examples:
make example

# getting help:
python3 -m automata --help
```

### Example (UFA)

#### ConfigFile.json

```json
{
  "states": ["q0", "q1", "q2", "q3"],
  "alphabet": ["0", "1"],
  "transitions": {
    "q0": {
      "0": ["q0", "q2"],
      "1": ["q1"]
    },
    "q1": {
      "0": ["q1"],
      "1": ["q2"]
    },
    "q2": {
      "0": ["q3"],
      "1": ["q0"]
    },
    "q3": {
      "1": ["q3"]
    }
  },
  "initial_state": "q0",
  "final_states": ["q3"]
}
```

#### Result

```bash
[--- ./path/to/config.json: ---]
length: 00       ambiguity: 0
length: 01       ambiguity: 1
length: 02       ambiguity: 1
length: 03       ambiguity: 1
length: 04       ambiguity: 1
length: 05       ambiguity: 1
length: 06       ambiguity: 1
length: 07       ambiguity: 1
length: 08       ambiguity: 1
length: 09       ambiguity: 1
length: 10       ambiguity: 1
length: 11       ambiguity: 1
length: 12       ambiguity: 1
length: 13       ambiguity: 1
length: 14       ambiguity: 1
[----------------------------]
```

## Testing, Linting, Cleaning

```bash
# test: pytest
make test

# lint: flake8
make lint

# clean: cache/tmp files
make clean
```
