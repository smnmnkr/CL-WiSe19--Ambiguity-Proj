import pytest

from automata.ambiguity import ambiguity_over_range, degree_of_ambiguity
from automata.nfa import NFA

automaton: NFA = NFA(**pytest.automata_config)


def test_degree_of_ambiguity():
    assert degree_of_ambiguity(automaton, 1) == ("a", 2)


def test_ambiguity_over_range():
    assert ambiguity_over_range(automaton, 3) == [("a", 2), ("aa", 1), ("aaa", 1)]
