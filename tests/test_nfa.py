from automata.nfa import NFA

config: dict = {
    'states': ['q0', 'q1', 'q2', 'q3'],
    'alphabet': ['a'],
    'transitions': {
        'q0': {
            'a': ['q1', 'q2', 'q3']
        },
        'q1': {
            'a': ['q1']
        }
    },
    'initial_state': 'q0',
    'final_states': ['q1', 'q2'],
}

automaton: NFA = NFA(**config)

word: str = 'a'

all_path: list = [['q0', 'q1'], ['q0', 'q2'], ['q0', 'q3']]
accepting_path: list = [['q0', 'q1'], ['q0', 'q2']]
ambiguity: int = 2


def test_init():
    assert type(automaton) == NFA


def test_export():
    assert automaton.export() == config


def test_process():
    assert list(automaton.process(word)) == all_path


def test_accepts():
    assert automaton.accepts(word)[0] == True
    assert automaton.accepts(word)[1] == accepting_path


def test_ambiguity():
    assert automaton.ambiguity(word) == ambiguity