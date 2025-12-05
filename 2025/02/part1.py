#!/usr/bin/env python
import functools
import logging
from math import log10
from typing import Any, Generator

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str) -> Generator[tuple[int, int], Any, None]:
    for pair in input_str.strip().split(','):
        l, r = pair.split('-')
        yield (int(l), int(r))
    return


def gen_ids() -> Generator[int]:
    n = 10
    while True:
        multiplier = 1 + n
        for i in range(n // 10, n):
            yield i * multiplier
        n *= 10


def is_valid(number: int, max_pairs: None) -> bool:
    digits = int(log10(number)) + 1
    pairs = 2
    while pairs <= digits:
        if digits % pairs != 0:
            pairs += 1
            continue
        if max_pairs and pairs > max_pairs:
            return False
        if number % calc_base(digits, pairs) == 0:
            return True
        pairs += 1
    return False


@functools.lru_cache(1024)
def calc_base(digits: int, pairs: int) -> int:
    digits_per_pair = digits // pairs
    base = 0
    for position in range(pairs):
        base += pow(10, digits_per_pair * position)
    return base


def brute_force_approach(ranges) -> int:
    total = 0

    end = max([r.stop for r in ranges])
    for number in gen_ids():
        if number > end:
            break
        if any(number in r for r in ranges):
            total += number
    return total


def verify_approach(ranges) -> int:
    total = 0
    for r in ranges:
        for number in r:
            if is_valid(number, 2):
                total += number
    return total


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    ranges = [range(l, r + 1) for l, r in data]

    # return brute_force_approach(ranges)
    return verify_approach(ranges)


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
