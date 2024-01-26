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
    logging.info(f'Parsing')
    for line in input_str.strip().splitlines():
        [begin, end] = line.split('~')
        b= Brick(
                Point(*map(int, begin.split(',')))
                ,
                Point(*map(int, end.split(',')))
            )
        if b.start.z > b.end.z:
            logging.info(f'need normalizing {b}')

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
    logging.info(f'Sorting')
    ordered_objects = sorted(data,
                             key=lambda x: min(x.start.z, x.end.z))

    logging.info(f'Calculating order')
    landed_objects = []
    collapsers=set()
    support_graph = defaultdict(list)
    # reverse of support graph
    rest_graph = defaultdict(set)
    for dropping in ordered_objects:
        pottential_supports = []
        for landed in landed_objects:
            if bricks_cross(landed, dropping):
                pottential_supports.append(landed)

        height = 0
        if pottential_supports:
            height = max([b.end.z for b in pottential_supports])
        obj_height = dropping.end.z - dropping.start.z

        dropped = Brick(
            Point(dropping.start.x, dropping.start.y, height+1),
            Point(dropping.end.x, dropping.end.y, height + 1+obj_height),
        )
        landed_objects.append(dropped)

        supporters = [b for b in pottential_supports if b.end.z == height]
        for supporter in supporters:
            support_graph[supporter].append(dropped)
        rest_graph[dropped] = set(supporters)

        if len(supporters) == 1:
            collapsers.add(supporters[0])


    logging.info(f'Counting collapses')
    @cache
    def traverse_graph(brick):
        bricks =set([brick])
        candidates = support_graph[brick].copy()

        while True:
            for brick in candidates:
                if rest_graph[brick].issubset(bricks):
                    candidates.remove(brick)
                    candidates.extend(support_graph[brick].copy())
                    bricks.add(brick)
                    break
            else:
                break
        return bricks

    def count_elements(brick):
        return len(traverse_graph(brick))-1
    counts = list(map(count_elements,collapsers))
    return sum(counts)



if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
