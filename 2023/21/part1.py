#!/usr/bin/env python
import logging
from collections import namedtuple
from dataclasses import dataclass
from functools import cache

Point = namedtuple('Point', ['x','y'])

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

directions = [
    (-1,0),
    (1, 0),
    (0, -1),
    (0, 1),
]

@dataclass(frozen=True)
class GardenMap:
    start: Point
    max: Point
    stones: set[Point]


def parse_input(input_str: str) -> GardenMap:
    start = None
    stones=set()
    for y, line in enumerate(input_str.strip().splitlines()):
        for x, char in enumerate(line):
            point = Point(x,y)
            if char == '#':
                stones.add(point)
            elif char == 'S':
                start = point
    return GardenMap(
        start=start,
        stones=frozenset(stones),
        max=Point(x,y)
    )

@cache
def findSteps(gardenMap:GardenMap, step:Point) -> set[Point]:
    next_steps=set()
    for dx,dy in directions:
        possible_step = Point(step.x + dx, step.y+dy)
        if possible_step in gardenMap.stones:
            continue
        next_steps.add(possible_step)
    
    return next_steps


def puzzle(input_str: str, max_steps:int) -> int:
    gardenMap = parse_input(input_str)
    steps=set( [gardenMap.start])
    for n in range(max_steps):
        next_steps=set()
        for step in steps:
            next_steps = next_steps.union(findSteps(gardenMap, step))
        steps = next_steps
    return len(steps)


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read(), 64))
