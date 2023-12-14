#!/usr/bin/env python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str):
    maps = []
    current_map = []
    for line in input_str.strip().splitlines():
        if not line:
            maps.append(current_map)
            current_map = []
            continue
        current_map.append(line)
    if current_map:
        maps.append(current_map)
    return maps


def find_mirror(land_map: list):
    for test_row in range(0, len(land_map) - 1):
        min_compare = test_row + 1
        max_compare = len(land_map) - test_row - 1
        compare_range = min(min_compare, max_compare)
        for compare in range(compare_range):
            if land_map[test_row - compare] != land_map[test_row + compare + 1]:
                break
        else:
            return test_row + 1


def rotate_map(land_map: list):
    return [
        ''.join([col[row] for col in land_map])
        for row in range(0, len(land_map[0]))
    ]


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    sum = 0
    for land_map in data:
        horizontal_mirror = find_mirror(land_map) or 0
        rotated_map = rotate_map(land_map)
        vertical_mirror = find_mirror(rotated_map) or 0
        sum += vertical_mirror + 100 * horizontal_mirror
    return sum


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
