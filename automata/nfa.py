class NFA(object):
    __slots__ = [
        'states',
        'alphabet',
        'transitions',
        'initial_state',
        'final_states',
    ]

    #
    #
    #  -------- Init -----------
    #
    def __init__(
            self,
            states: set,
            alphabet: set,
            transitions: dict,
            initial_state: str,
            final_states: set,
    ):
        """
            Initialize a complete automaton.
        """

        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    #
    #
    #  -------- validate -----------
    #
    def validate(self):
        """Return True if this automaton is internally consistent."""
        raise NotImplementedError

    #
    #
    #  -------- process -----------
    #
    def process(self, word, ):
        """
        Check if the given string is accepted by this automaton.
        Return all accepting paths.
        """
        

        for char in word:
            pass

    #  -------- export -----------
    #
    def export(self):
        return {
            'states': self.states,
            'alphabet': self.alphabet,
            'transitions': self.transitions,
            'initial_state': self.initial_state,
            'final_states': self.final_states,
        }

    #  -------- __eq__ -----------
    #
    def __eq__(self, other):
        """Check if two automata are equal."""
        return vars(self) == vars(other)