#!/usr/bin/env python
import logging
from collections import defaultdict

from part1 import parse_input

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    # Key is a beam position, value is number of timelines it exists in
    beams: dict[int,int] = {data['start'][1]: 1}
    y = 0
    while True:
        y = y + 1
        if y > data['height'] - 1:
            break
        new_beams = defaultdict(int)
        for x, timelines in beams.items():
            # Reached end
            if x in data['splitters'][y]:
                new_beams[x - 1] += timelines
                new_beams[x + 1] += timelines
            else:
                new_beams[x] += timelines
        beams = new_beams

    return sum(beams.values())


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
