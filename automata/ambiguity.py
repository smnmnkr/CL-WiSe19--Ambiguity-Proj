from automata.nfa import NFA
from automata.util import create_permutations


# -------- ambiguity_over_range -----------
#
def ambiguity_over_range(
        automaton: NFA,
        maximum: int,
        minimum: int = 1,
) -> list:

    return [
        degree_of_ambiguity(automaton, n) for n in range(minimum, maximum + 1)
    ]


# -------- degree_of_ambiguity -----------
#
def degree_of_ambiguity(automaton: NFA, length: int) -> tuple:

    max_word: str = ''
    max_path_num: int = 0

    for word in create_permutations(automaton.alphabet, length):

        word_ambiguity: int = automaton.ambiguity(word)

        if (max_path_num < word_ambiguity):
            max_word = word
            max_path_num = word_ambiguity

    return max_word, max_path_num
