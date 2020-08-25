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
    'final_states': ['q1', 'q2'],
}

word: str = 'a'
automaton: NFA = NFA(**config)


def test_init():
    assert type(automaton) == NFA


def test_export():
    assert automaton.export() == config


def test_process():
    assert list(automaton.process(word)) == [['q0', 'q1'], ['q0', 'q2']]


def test_accepts():
    assert automaton.accepts(word) == True


def test_ambiguity():
    assert automaton.ambiguity(word) == 2