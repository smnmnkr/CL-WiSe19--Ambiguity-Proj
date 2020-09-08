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
        Returns all possible traces.
        """

        # start processing with initial state
        if not trace:
            trace.append(self.initial_state)

        # get the current state transitions
        state_transition: dict = self.transitions.get(trace[-1], None)

        # processing aborted; input not accepted
        if not state_transition:
            return

        # begin recursive processing
        if word:
            # iterate over each possible transition
            for state in state_transition.get(word[0], []):

                # create new sub trace, append current state
                sub_trace: list = trace.copy()
                sub_trace.append(state)

                # start recursive function call
                yield from self.process(word[1:], trace=sub_trace)

        # processing finished; input accepted
        else:
            yield trace

    #
    #
    #  -------- accepts -----------
    #
    def accepts(self, word: str) -> (bool, list):
        """
        Proccess the given string in the automaton.
        Returns if string is accepted and every accepting path.
        """

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
        """
        Proccess the given string in the automaton.
        Returns the number of accepting path.
        """

        _a, accepting_path = self.accepts(word)

        return len(accepting_path)

    #  --------__dict__ -----------
    #
    @property
    def __dict__(self):
        return super().__dict__
