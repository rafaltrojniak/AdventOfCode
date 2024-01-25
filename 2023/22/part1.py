#!/usr/bin/env python
import logging
from typing import NamedTuple
from functools import cache
from collections import defaultdict


class Point(NamedTuple):
    x: int
    y: int
    z: int


class Brick(NamedTuple):
    start: Point
    end: Point


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str):
    objects = []
    for line in input_str.strip().splitlines():
        [begin, end] = line.split('~')
        b= Brick(
                Point(*map(int, begin.split(',')))
                ,
                Point(*map(int, end.split(',')))
            )
        assert b.start.z <= b.end.z

        objects.append(b)
    return objects


@cache
def lines_cross(a:tuple[int,int], b:tuple[int,int]):
    a_min,a_max = sorted(a)
    b_min,b_max = sorted(b)
    return a_min <= b_min <= a_max or \
       a_min <= b_max <= a_max or \
       b_min <= a_min <= b_max or \
       b_min <= a_max <= b_max

@cache
def bricks_cross(a: Brick, b: Brick):
    return \
        lines_cross(
            (a.start.x, a.end.x),
            (b.start.x, b.end.x)
        ) \
        and \
        lines_cross(
            (a.start.y, a.end.y),
            (b.start.y, b.end.y)
        )


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    ordered_objects = sorted(data,
                             key=lambda x: min(x.start.z, x.end.z))

    landed_objects = []
    supporters_set = set()
    for dropping in ordered_objects:
        this_supporting=set()
        pottential_supports = []
        for landed in landed_objects:
            if bricks_cross(landed, dropping):
                logging.info(f'{landed} supports {dropping}')
                pottential_supports.append(landed)
        height=0
        if pottential_supports:
            height = max([b.end.z for b in pottential_supports])
        supporters = [b for b in pottential_supports if b.end.z == height]
        supporters_set.add(frozenset(supporters))

        obj_height = dropping.end.z - dropping.start.z
        dropped = Brick(
            Point(dropping.start.x, dropping.start.y, height+1),
            Point(dropping.end.x, dropping.end.y, height + 1+obj_height),
        )
        landed_objects.append(dropped)

    non_supporting_counter = 0
    for obj in landed_objects:
        if frozenset([obj]) not in  supporters_set:
            non_supporting_counter+=1

    return non_supporting_counter



if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
