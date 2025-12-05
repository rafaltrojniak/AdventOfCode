#!/usr/bin/env python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str):
    for line in input_str.strip().split('\n'):
        yield [int(char) for char in line.strip()]


def maximal_joltage(row: list[int]):
    if len(row) < 2:
        return 0

    return max(row[0] * 10 + max(row[1:]), maximal_joltage(row[1:]))


def brute_force_solution(data):
    total = 0
    for row in data:
        total += maximal_joltage(row)
    return total


def puzzle(input_str: str) -> int:
    data = list(parse_input(input_str))
    return brute_force_solution(data)


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
