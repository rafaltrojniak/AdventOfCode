#!/usr/bin/env python
import logging
from functools import reduce
from typing import Generator

from part1 import OPERATIONS

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str):
    data = []
    for line in input_str.split('\n'):
        data.append(line)
    # Remove the empty at the end of the file
    while data[-1].strip() == '':
        data.pop(-1)

    # Pad each line with spaces so they are all the same length
    max_line = max(len(line) for line in data)
    for i in range(len(data)):
        data[i] = data[i].ljust(max_line)
    return data


def convert_cephalopod_to_human(celophad: list[str]) -> Generator[tuple[str, list[int]]]:
    control_line = celophad[-1]
    current_action = ''
    current_numbers = []
    for x in range(len(celophad[0])):

        if control_line[x] != ' ':
            if current_numbers:
                yield current_action, current_numbers
            current_action = control_line[x]
            current_numbers = []

        number = extract_celophad_number(celophad, x)
        if number:
            current_numbers.append(number)

    yield current_action, current_numbers


def extract_celophad_number(celophad: list[str], x: int) -> int:
    number = 0
    for y in range(len(celophad) - 1):
        char = celophad[y][x]
        if char == ' ':
            continue
        number = number * 10 + int(char)
    return number


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    total = 0
    for action, numbers in convert_cephalopod_to_human(data):
        result = reduce(OPERATIONS[action], numbers[1:], numbers[0])
        total += result
    return total


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))