from abc import ABC, abstractmethod


class Automaton(ABC):
    __slots__ = [
        "states",
        "alphabet",
        "transitions",
        "initial_state",
        "final_states",
    ]

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

        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    #  -------- process -----------
    #
    @abstractmethod
    def process(self, word: str, trace: list = []) -> list:
        raise NotImplementedError

    #  -------- accepts -----------
    #
    @abstractmethod
    def accepts(self, word: str) -> (bool, list):
        raise NotImplementedError

    #  -------- __eq__ -----------
    #

    def __eq__(self, other) -> bool:
        return vars(self) == vars(other)

    #  --------__dict__ -----------
    #
    @property
    def __dict__(self):
        return {s: getattr(self, s, None) for s in self.__slots__}
