from automata.nfa import NFA
from automata.tasks import ambiguity_over_range

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

print("---[ ambiguity of ENA example: ]---")
ambiguity_over_range(ena, 15)
print("\n")
