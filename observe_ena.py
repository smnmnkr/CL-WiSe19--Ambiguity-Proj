from automata.nfa import NFA
from automata.util import create_permutations

# src:
# Relating the Type of Ambiguity of Finite Automata to the Succinctness of Their Representation
# Fig. 2.: Example of a strictly exponentially ambiguous nfa. (p. 1267/5)
#
config: dict = {
    'states': ['q0', 'q1', 'q2', 'q3', 'q4', 'q5'],
    'alphabet': ['a', 'b'],
    'transitions': {
        'q0': {
            'b': ['q1', 'q4']
        },
        'q1': {
            'a': ['q2'],
            'b': ['q0']
        },
        'q2': {
            'a': ['q3']
        },
        'q3': {
            'a': ['q1']
        },
        'q4': {
            'a': ['q5'],
            'b': ['q0']
        },
        'q5': {
            'a': ['q4']
        }
    },
    'initial_state': 'q0',
    'final_states': ['q0'],
}

ena: NFA = NFA(**config)

for n in range(1, 16):

    max_path_num: int = 0

    for word in create_permutations(ena.alphabet, n):

        word_ambiguity: int = ena.ambiguity(word)

        if (max_path_num < word_ambiguity):
            max_path_num = word_ambiguity

    print(f"length: {n:02}\t ambiguity: {max_path_num}")