#!/usr/bin/env python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str):
    return input_str.strip().split(',')


def hash(src: str) -> int:
    acc = 0
    for char in src:
        acc += ord(char)
        acc = acc * 17 % 256
    return acc


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    return sum(
        map(hash, data)
    )


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
