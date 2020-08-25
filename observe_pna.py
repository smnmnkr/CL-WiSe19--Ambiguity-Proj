from automata.nfa import NFA
from automata.util import create_permutations

# src:
# Relating the Type of Ambiguity of Finite Automata to the Succinctness of Their Representation
# Fig. 1.: Example of astrictly polynomially ambiguous nfa.
#
config: dict = {
    'states': ['q0', 'q1', 'q2', 'q3', 'q4'],
    'alphabet': ['0', '1'],
    'transitions': {
        'q0': {
            '0': ['q0'],
            '1': ['q0', 'q1']
        },
        'q1': {
            '0': ['q2'],
            '1': ['q2']
        },
        'q2': {
            '0': ['q3'],
            '1': ['q3']
        },
        'q3': {
            '1': ['q4']
        },
        'q4': {
            '0': ['q4'],
            '1': ['q4']
        }
    },
    'initial_state': 'q0',
    'final_states': ['q4'],
}

ena: NFA = NFA(**config)

for n in range(1, 16):

    max_path_num: int = 0

    for word in create_permutations(ena.alphabet, n):

        word_ambiguity: int = ena.ambiguity(word)

        if (max_path_num < word_ambiguity):
            max_path_num = word_ambiguity

    print(f"length: {n:02}\t ambiguity: {max_path_num}")