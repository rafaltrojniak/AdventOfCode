#!/usr/bin/env python
import logging
from itertools import combinations

from part1 import parse_input

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def joltage(numbers):
    numbers = list(numbers)
    acc = 0
    acc += numbers.pop(0)
    while numbers:
        acc *= 10
        acc += numbers.pop(0)
    return acc


def brute_force_solution(data):
    return [max([joltage(x) for x in combinations(row, 12)]) for row in data]


def max_in_row(data: list[int], left=12):
    if left == 1:
        return max(data)
    number = max(data[0:(1 - left)])
    position = data.index(number)
    return number * pow(10, left - 1) + max_in_row(data[position + 1:], left - 1)


def puzzle(input_str: str) -> int:
    data = list(parse_input(input_str))
    # brute_force_values = brute_force_solution(data)
    # return sum(brute_force_values)
    analytical_values = [max_in_row(row) for row in data]
    return sum(analytical_values)


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
