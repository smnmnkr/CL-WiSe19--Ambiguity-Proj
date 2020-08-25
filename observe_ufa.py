from automata.nfa import NFA
from automata.tasks import ambiguity_over_range

# src:
# DESCRIPTIONAL COMPLEXITY OF NFA OF DIFFERENT AMBIGUITY
# Fig. 1.: UFA U4 (p. 997/3)
#
config: dict = {
    'states': ['q0', 'q1', 'q2', 'q3'],
    'alphabet': ['0', '1'],
    'transitions': {
        'q0': {
            '0': ['q0', 'q2'],
            '1': ['q1']
        },
        'q1': {
            '0': ['q1'],
            '1': ['q2']
        },
        'q2': {
            '0': ['q3'],
            '1': ['q0']
        },
        'q3': {
            '1': ['q3']
        }
    },
    'initial_state': 'q0',
    'final_states': ['q3'],
}

ufa: NFA = NFA(**config)
ambiguity_over_range(ufa, 15)
