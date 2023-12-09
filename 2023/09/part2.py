import logging
from itertools import pairwise, tee, islice

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str):
    return [
        [int(n) for n in line.strip().split(' ')]
        for line in input_str.strip().splitlines()
    ]


def find_missing_element(sequence: list) -> int:
    deltas = [j - i for i, j in pairwise(sequence)]
    if any(deltas):
        new_delta = find_missing_element(deltas)
    else:
        new_delta = 0
    return sequence[-1] + new_delta


# Just an experiment - running the same function on generators / iterators only.
# This makes it able to run on huge ranges,
# and compute only what is needed
def find_missing_element_with_itreators(sequence: list) -> int:
    return reversed_find_missing_element_with_iterators(reversed(sequence))


def reversed_find_missing_element_with_iterators(sequence: list):
    find_deltas_it, get_first_it = tee(sequence)

    deltas = map(lambda t: t[0] - t[1], pairwise(find_deltas_it))
    deltas_for_checking_it, deltas_for_passing_it = tee(deltas)

    if any(islice(deltas_for_checking_it, 5)):
        new_delta = reversed_find_missing_element_with_iterators(deltas_for_passing_it)
    else:
        new_delta = 0
    first_element = list(islice(get_first_it, 1))[0]
    return first_element + new_delta


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    reversed_data = [serie[::-1] for serie in data]
    missing_elements = list(map(find_missing_element, reversed_data))
    # missing_elements = list(map(reversed_find_missing_element_with_iterators, reversed_data))

    return sum(missing_elements)


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
