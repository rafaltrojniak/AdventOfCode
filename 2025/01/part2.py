#!/usr/bin/env python
import logging
from part1 import parse_input

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def puzzle(input_str: str) -> int:
    data = list(parse_input(input_str))
    count=0
    position=50
    for dir, amount in data:
        if dir == 'R':
            for _ in range(amount):
                position +=1
                position %=100
                if not position: count+=1
        elif dir == 'L' :
            for _ in range(amount):
                position -=1
                if position < 0:
                    position +=100
                if not position: count+=1
    return count


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
