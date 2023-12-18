#!/usr/bin/env python
import logging
import re
from itertools import pairwise

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str):
    pattern = re.compile('(.) ([0-9]*) \\(#([a-f0-9]*)\\)')
    matches = [ tuple(pattern.match(line).groups()) for line in input_str.strip().splitlines() ]
    return [ (letter, int(depth), color) for letter, depth, color in matches]

DIRECTIONS={
    'R': (1,0),
    'L': (-1, 0),
    'D': (0, 1),
    'U': (0, -1),
}

def print_map(digs:set, min_x:int, max_x:int, min_y:int, max_y:int):

    print()
    for y in range(min_y,max_y+1):
        for x in range(min_x,max_x+1):
            point = (x,y)
            if point in digs:
                print('#', end='')
            else:
                print('.', end='')
        print()


LEFT_SIDE_GRADIENT = {
    (0, 1): (1, 0),
    (0, -1): (-1, 0),
    (1, 0): (0, -1),
    (-1, 0): (0, 1)
}
RIGHT_SIDE_GRADIENT = {
    (0, 1): (-1, 0),
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (-1, 0): (0, -1)
}

def get_positions_on_one_side_of_the_path(path: list, gradient: dict):
    path_set = set(path)
    points_on_the_side = set()
    for last_node, next_node in pairwise(path):
        move_gradient = (next_node[0] - last_node[0],
                         next_node[1] - last_node[1])
        side_gradient = gradient[move_gradient]
        side_node = (next_node[0] + side_gradient[0], next_node[1] + side_gradient[1])
        if side_node in path_set:
            continue
        points_on_the_side.add(side_node)
    return points_on_the_side

def expand_on_neighbour_tiles(inside_area_to_check: set[tuple[int, int]], path: list[tuple[int, int]],
                              size: tuple[int, int]):
    path_set = set(path)
    inside_area_checked = inside_area_to_check.copy()
    while inside_area_to_check:
        node = inside_area_to_check.pop()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            candidate = (node[0] + dx, node[1] + dy)
            if candidate in path_set:
                continue
            if candidate in inside_area_checked:
                continue
            inside_area_checked.add(candidate)
            inside_area_to_check.add(candidate)
            if node[0] > size[0] or node[1] > size[1]:
                raise Exception(f'got out of the board at {node=}')
    return inside_area_checked

def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    digs = list()
    x,y=(0,0)
    for direction, length, _color in data:
        dx, dy = DIRECTIONS[direction]
        while length:
            length-=1
            x=x+dx
            y=y+dy
            digs.append( (x,y) )
    max_x=max(x for x,_y in digs)
    max_y=max(y for _x,y in digs)
    min_x=min(x for x,_y in digs)
    min_y=min(y for _x,y in digs)

    print_map(set(digs), min_x,max_x, min_y, max_y)

    inside_area_to_check = get_positions_on_one_side_of_the_path(digs, RIGHT_SIDE_GRADIENT)
    inside_area_to_check = inside_area_to_check.union(
        get_positions_on_one_side_of_the_path(digs[::-1], LEFT_SIDE_GRADIENT))

    inside_area_checked = expand_on_neighbour_tiles(inside_area_to_check, digs, (max_x+1,max_y+1))

    return len(inside_area_checked) + len(digs)



if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
