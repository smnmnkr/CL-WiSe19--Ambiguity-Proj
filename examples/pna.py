from automata.nfa import NFA
from automata.tasks import ambiguity_over_range

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

pna: NFA = NFA(**config)

print("---[ ambiguity of PNA example: ]---")
ambiguity_over_range(pna, 15)
print("\n")
