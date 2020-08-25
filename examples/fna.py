from automata.nfa import NFA
from automata.tasks import ambiguity_over_range

# src:
# Relating the Type of Ambiguity of Finite Automata to the Succinctness of Their Representation
# Fig. 6.: An fna accepting L3 (p. 1271/9)
#
config: dict = {
    'states':
    ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10'],
    'alphabet': ['a'],
    'transitions': {
        'q0': {
            'a': ['q1', 'q3', 'q6']
        },
        'q1': {
            'a': ['q2']
        },
        'q2': {
            'a': ['q1']
        },
        'q3': {
            'a': ['q4']
        },
        'q4': {
            'a': ['q5']
        },
        'q5': {
            'a': ['q3']
        },
        'q6': {
            'a': ['q7']
        },
        'q7': {
            'a': ['q8']
        },
        'q8': {
            'a': ['q9']
        },
        'q9': {
            'a': ['q10']
        },
        'q10': {
            'a': ['q6']
        }
    },
    'initial_state': 'q0',
    'final_states': ['q1', 'q3', 'q4', 'q6', 'q7', 'q8', 'q9'],
}

fna: NFA = NFA(**config)

print("---[ ambiguity of FNA example: ]---")
ambiguity_over_range(fna, 15)
print("\n")
