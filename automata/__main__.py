import json
import argparse

from automata.nfa import NFA
from automata.ambiguity import ambiguity_over_range

from automata.util import time_track

#
#
#  -------- ARGPARSER -----------
#
parser = argparse.ArgumentParser(description='run automata class')

# argument: config file
parser.add_argument(
    'configFile',
    metavar='configFile',
    help='path to configuration json',
    type=str,
    nargs='?',
)

# argument: config file
parser.add_argument(
    '-l',
    dest='length',
    help='maximal word length to test',
    type=int,
    nargs='?',
    default=15,
)


def task__ambiguity_over_range(config: dict, length: int) -> None:

    automata: NFA = NFA(**config)
    data, duration = time_track(ambiguity_over_range)(automata, length)

    print(f"[--- {args.configFile}: ---]")

    for n, row in enumerate(data):
        print(f"length: {n+1:02}\t ambiguity: {row[1]}")

    print(f"[--- duration: {duration:2.4f} sec ---]\n")


#
#
#  -------- __main__ -----------
#
if __name__ == '__main__':

    # collect terminal parameters
    args = parser.parse_args()

    # load JSON config
    with open(args.configFile) as json_file:
        config = json.load(json_file)

    # run ambiguity task
    task__ambiguity_over_range(config, args.length)
