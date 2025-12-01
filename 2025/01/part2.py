#!/usr/bin/env python
import logging
from pprint import pprint

from part1 import parse_input

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def bruteforce_approach(data: list[tuple[str, int]]):
    count = 0
    position = 50
    for dir, amount in data:
        if dir == 'R':
            for _ in range(amount):
                position += 1
                position %= 100
                if not position: count += 1
        elif dir == 'L':
            for _ in range(amount):
                position -= 1
                if position < 0:
                    position += 100
                if not position: count += 1
    return count


def analytical_approach(data: list[tuple[str, int]]):
    position, count = 50, 0
    for direction, amount in data:
        amount = -amount if direction == 'L' else amount
        old_position = position
        position += amount

        if position * old_position < 0:  # Crossed zero
            count += 1
        if position == 0:  # Stayed at zero
            count += 1
        if abs(position) >= 100:  # Rolled over multiple times
            count += abs(position) // 100
            position %= 100
        if position<0:
            position +=100

    return count


def puzzle(input_str: str) -> int:
    data = list(parse_input(input_str))
    bruteforce = bruteforce_approach(data)
    analytical = analytical_approach(data)

    assert bruteforce == analytical

    return analytical


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
