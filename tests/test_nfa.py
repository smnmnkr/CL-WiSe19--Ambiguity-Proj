from automata.nfa import NFA

config: dict = {
    'states': ['q0', 'q1', 'q2'],
    'alphabet': ['a'],
    'transitions': {
        'q0': {
            'a': ['q1', 'q2']
        },
        'q1': {
            'a': ['q1']
        }
    },
    'initial_state': 'q0',
    'final_states': ['q1'],
}

testNFA = NFA(**config)


def test_init():
    assert testNFA.export() == config


def test_process():
    assert list(testNFA.process("a")) == [['q0', 'q1'], ['q0', 'q2']]
