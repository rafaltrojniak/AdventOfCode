#!/usr/bin/env python
import logging
from functools import reduce

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str):
    data = []
    for line in input_str.strip().split('\n'):
        row = []
        for item in line.split():
            if item in ('+', '-', '*', '/'):
                row.append(item)
            else:
                row.append(int(item))
        data.append(row)
    return data


OPERATIONS = {'+': int.__add__, '-': int.__sub__, '*': int.__mul__, '/': int.__floordiv__}


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    total = 0
    for x in range(len(data[0])):
        action = data[-1][x]
        result = reduce(OPERATIONS[action], [row[x] for row in data[1:-1]], data[0][x])
        total += result
    return total


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
