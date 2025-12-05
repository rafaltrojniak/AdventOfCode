#!/usr/bin/env python
import logging

from part1 import parse_input, is_valid

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    ranges = [range(l, r + 1) for l, r in data]
    total = 0

    for r in ranges:
        for number in r:
            if is_valid(number, None):
                total += number
    return total


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
