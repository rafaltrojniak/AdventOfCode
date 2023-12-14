#!/usr/bin/env python
import logging
from dataclasses import dataclass
from functools import cache
from pprint import pprint

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


@dataclass(frozen=True)
class Rock_map:
    max_x: int
    max_y: int
    rocks: frozenset
    stops: frozenset

    def print(self):
        print('---')
        for y in range(self.max_y):
            for x in range(self.max_x):
                point = (x, y)
                if point in self.rocks:
                    print('O', end='')
                elif point in self.stops:
                    print('#', end='')
                else:
                    print('.', end='')
            print()


def parse_input(input_str: str):
    rocks = set()
    stops = set()
    lines = input_str.strip().splitlines()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                stops.add((x, y))
            elif char == 'O':
                rocks.add((x, y))
    return Rock_map(
        max_x=len(lines[0]),
        max_y=len(lines),
        rocks=frozenset(rocks),
        stops=frozenset(stops)
    )


def print_rocks(rocks_map):
    print(
        '\n' + '\n'.join([''.join(line) for line in rocks_map])
    )


@cache
def tilt_plate_up(rock_map: Rock_map):
    new_rock_map = set()
    for x in range(rock_map.max_x):
        last_position = 0
        for y in range(rock_map.max_y):
            point = (x, y)
            if point in rock_map.stops:
                last_position = y + 1
            elif point in rock_map.rocks:
                new_rock_position = (x, last_position)
                if new_rock_position in new_rock_map \
                        or new_rock_position in rock_map.stops:
                    raise Exception(f'Rock piled up at {y}{x}')
                new_rock_map.add(new_rock_position)
                last_position += 1
    return Rock_map(
        max_x=rock_map.max_x,
        max_y=rock_map.max_y,
        stops=rock_map.stops,
        rocks=frozenset(new_rock_map)
    )


@cache
def tilt_plate_down(rock_map: Rock_map):
    new_rock_map = set()
    for x in range(rock_map.max_x):
        last_position = rock_map.max_x - 1
        for y in reversed(range(rock_map.max_y)):
            point = (x, y)
            if point in rock_map.stops:
                last_position = y - 1
            elif point in rock_map.rocks:
                new_rock_position = (x, last_position)
                if new_rock_position in new_rock_map \
                        or new_rock_position in rock_map.stops:
                    raise Exception(f'Rock piled up at {y}{x}')
                new_rock_map.add(new_rock_position)
                last_position -= 1
    return Rock_map(
        max_x=rock_map.max_x,
        max_y=rock_map.max_y,
        stops=rock_map.stops,
        rocks=frozenset(new_rock_map)
    )


@cache
def tilt_plate_left(rock_map: Rock_map):
    new_rock_map = set()
    for y in range(rock_map.max_y):
        last_position = 0
        for x in range(rock_map.max_x):
            point = (x, y)
            if point in rock_map.stops:
                last_position = x + 1
            elif point in rock_map.rocks:
                new_rock_position = (last_position, y)
                if new_rock_position in new_rock_map \
                        or new_rock_position in rock_map.stops:
                    raise Exception(f'Rock piled up at {y}{x}')
                new_rock_map.add(new_rock_position)
                last_position += 1
    return Rock_map(
        max_x=rock_map.max_x,
        max_y=rock_map.max_y,
        stops=rock_map.stops,
        rocks=frozenset(new_rock_map)
    )


@cache
def tilt_plate_right(rock_map: Rock_map):
    new_rock_map = set()
    for y in range(rock_map.max_y):
        last_position = rock_map.max_y - 1
        for x in reversed(range(rock_map.max_x)):
            point = (x, y)
            if point in rock_map.stops:
                last_position = x - 1
            elif point in rock_map.rocks:
                new_rock_position = (last_position, y)
                if new_rock_position in new_rock_map \
                        or new_rock_position in rock_map.stops:
                    raise Exception(f'Rock piled up at {y}{x}')
                new_rock_map.add(new_rock_position)
                last_position -= 1
    return Rock_map(
        max_x=rock_map.max_x,
        max_y=rock_map.max_y,
        stops=rock_map.stops,
        rocks=frozenset(new_rock_map)
    )


def calc_wight(rock_map: Rock_map):
    stone_weight = 0
    for stone in rock_map.rocks:
        stone_weight += rock_map.max_y - stone[1]
    return stone_weight


@cache
def cycle(rock_map: Rock_map):
    # rock_map.print()
    # print('move up')
    rock_map = tilt_plate_up(rock_map)
    # rock_map.print()
    # print('move left')
    rock_map = tilt_plate_left(rock_map)
    # rock_map.print()
    # print('move down')
    rock_map = tilt_plate_down(rock_map)
    # rock_map.print()
    # print('move right')
    rock_map = tilt_plate_right(rock_map)
    # rock_map.print()
    return rock_map


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    results_set = {data}
    result_history = []
    target = 1_000_000_000
    for iteration in range(target):
        data = cycle(data)
        if data in results_set:
            last_index = result_history.index(data)
            delta = iteration - last_index
            offset = (target - last_index) % delta
            match = last_index + offset - 1
            return calc_wight(result_history[match])
        results_set.add(data)
        result_history.append(data)
        if iteration % 1_000_000 == 0:
            print(f'{iteration=}')
            pprint(cycle.cache_info())
    return calc_wight(data)


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
