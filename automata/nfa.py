from automata.automaton import Automaton


class NFA(Automaton):

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
        super().__init__(
            states, alphabet, transitions, initial_state, final_states
        )

    #
    #
    #  -------- process -----------
    #
    def process(self, word: str, trace: list = []) -> list:
        """
        Proccess the given string in the automaton.
        Return all possible paths.
        """

        # processing finished returning the trace
        if not word:
            yield trace

        # start processing with initial state
        if not trace:
            trace.append(self.initial_state)

        # get the current state transitions
        state_transition: dict = self.transitions.get(trace[-1], None)

        # input not accepted
        if not state_transition:
            return

        # get first letter else empty string
        first_letter: str = word[0] if (word) else ""

        # iterate over each possible transition
        for state in state_transition.get(first_letter, []):

            # create new sub trace, append current state
            sub_trace: list = trace.copy()
            sub_trace.append(state)

            # start recursive function call
            yield from self.process(word[1:], trace=sub_trace)

    #
    #
    #  -------- accepts -----------
    #
    def accepts(self, word: str) -> (bool, list):

        accepting: bool = False
        accepting_path: list = []

        for path in self.process(word):
            if path[-1] in self.final_states:
                accepting = True
                accepting_path.append(path)

        return accepting, accepting_path

    #  -------- ambiguity -----------
    #
    def ambiguity(self, word: str) -> int:

        _a, accepting_path = self.accepts(word)

        return len(accepting_path)

    #  --------__dict__ -----------
    #
    @property
    def __dict__(self):
        return super().__dict__
