import pytest

from automata.language import generate_language, language_over_range
from automata.nfa import NFA

automaton: NFA = NFA(**pytest.automata_config)


def test_generate_language():
    assert generate_language(automaton, 1) == ["a"]


def test_language_over_range():
    assert language_over_range(automaton, 3) == [
        ["a"],
        ["aa"],
        ["aaa"],
    ]
