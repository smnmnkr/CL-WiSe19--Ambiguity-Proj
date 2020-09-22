import argparse
import json

from automata.ambiguity import ambiguity_over_range
from automata.language import language_over_range
from automata.nfa import NFA
from automata.util import time_track

#
#
#  -------- ARGPARSER -----------
#
parser = argparse.ArgumentParser(description="run automata class")

# argument: config file
parser.add_argument(
    "configFile",
    metavar="configFile",
    help="path to configuration json",
    type=str,
    nargs="?",
)

# argument: config file
parser.add_argument(
    "-l",
    dest="length",
    help="maximal word length to test",
    type=int,
    nargs="?",
    default=15,
)


#  -------- task__ambiguity_over_range -----------
#
def task__ambiguity_over_range(automaton: NFA, length: int) -> None:

    data, duration = time_track(ambiguity_over_range)(automaton, length)

    print(f"[--- ambiguity: {args.configFile}: ---]")

    for n, row in enumerate(data):
        print(f"length: {n+1:02}\t ambiguity: {row[1]}")

    print(f"[--- duration: {duration:2.4f} sec ---]\n")


#  -------- task__language_over_range -----------
#
def task__language_over_range(automaton: NFA, length: int) -> None:

    data, duration = time_track(language_over_range)(automaton, length)

    print(f"[--- language: {args.configFile}: ---]")

    for n, row in enumerate(data):

        print(
            f"length: {n+1:02}\t language: |{len(row):05}| : {row[:5]}{'...' if len(row) > 5 else ''}"
        )

    print(f"[--- duration: {duration:2.4f} sec ---]\n")


#
#
#  -------- __main__ -----------
#
if __name__ == "__main__":

    # collect terminal parameters
    args = parser.parse_args()

    # load JSON config
    with open(args.configFile) as json_file:
        config = json.load(json_file)

    # init automaton
    automaton: NFA = NFA(**config)

    # run tasks
    task__ambiguity_over_range(automaton, args.length)
    task__language_over_range(automaton, args.length)
