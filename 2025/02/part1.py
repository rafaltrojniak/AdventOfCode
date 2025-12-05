#!/usr/bin/env python
import logging
from typing import Any, Generator

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str) -> Generator[tuple[int, int], Any, None]:
    for pair in input_str.strip().split(','):
        l,r=pair.split('-')
        yield (int(l),int(r))
    return

def gen_ids() -> Generator[int]:
    n=10
    while True:
        multiplier = 1+n
        for i in range(n//10,n):
            yield i*multiplier
        n*=10

def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    ranges = [ range(l,r+1) for l,r in data]
    end = max([r.stop for r in ranges])
    total = 0
    for number in gen_ids():
        if number > end:
            break
        if any( number in r for r in ranges):
            print(number)
            total += number
    return total


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
