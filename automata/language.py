from automata.nfa import NFA
from automata.util import create_permutations


#  -------- language_over_range -----------
#
def language_over_range(
    automaton: NFA, maximum: int, minimum: int = 1
) -> list:

    return [
        generate_language(automaton, n) for n in range(minimum, maximum + 1)
    ]


#  -------- generate_language -----------
#
def generate_language(automaton: NFA, length: int) -> list:

    return [
        x
        for x in create_permutations(automaton.alphabet, length)
        if automaton.accepts(x) != (False, [])
    ]
