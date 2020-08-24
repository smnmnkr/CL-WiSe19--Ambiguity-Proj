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
    def process(self, word: str, trace: list = []):
        """
        Check if the given string is accepted by this automaton.
        Return all accepting paths.
        """

        if (not word):
            print(trace)
            return trace

        if (not trace):
            trace.append(self.initial_state)

        state_transition: dict = self.transitions.get(trace[-1], None)

        if (not state_transition):
            return trace

        for state in state_transition.get(word[0], []):

            # create new sub trace, append current state
            sub_trace: list = trace.copy()
            sub_trace.append(state)

            self.process(word[1:], trace=sub_trace)

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