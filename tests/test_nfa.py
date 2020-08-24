from automata.nfa import NFA

config: dict = {
    'states': ['q0', 'q1'],
    'alphabet': ['a'],
    'transitions': {
        'q0': {
            'a': 'q1'
        },
        'q1': {
            'a': 'q1'
        }
    },
    'initial_state': 'q0',
    'final_states': ['q1'],
}


def test_init():

    testNFA = NFA(**config)

    assert testNFA.export() == config
