import pytest


def pytest_configure():
    pytest.automata_config: dict = {
        "states": ["q0", "q1", "q2", "q3"],
        "alphabet": ["a"],
        "transitions": {
            "q0": {"a": ["q1", "q2", "q3"]},
            "q1": {"a": ["q1"]},
        },
        "initial_state": "q0",
        "final_states": ["q1", "q2"],
    }
