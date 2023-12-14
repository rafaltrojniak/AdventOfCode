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
    mirrors = set()
    for test_row in range(0, len(land_map) - 1):
        min_compare = test_row + 1
        max_compare = len(land_map) - test_row - 1
        compare_range = min(min_compare, max_compare)
        for compare in range(compare_range):
            if land_map[test_row - compare] != land_map[test_row + compare + 1]:
                break
        else:
            mirrors.add(test_row + 1)
    return mirrors


def rotate_map(land_map: list):
    return [
        ''.join([col[row] for col in land_map])
        for row in range(0, len(land_map[0]))
    ]


def find_mirror_lines(land_map) -> tuple[set, set]:
    horizontal_mirror = find_mirror(land_map)
    rotated_map = rotate_map(land_map)
    vertical_mirror = find_mirror(rotated_map)
    return vertical_mirror, horizontal_mirror
    return vertical_mirror + 100 * horizontal_mirror


def find_corrected_mirror(org_land_map: list):
    land_map = [list(line) for line in org_land_map]
    org_vertical_mirror, org_horizontal_mirror = find_mirror_lines(land_map)
    copy_land_map = land_map.copy()
    found_mirrors = []
    for y in range(0, len(land_map)):
        for x in range(0, len(land_map[0])):
            copy_land_map[y] = land_map[y].copy()
            if copy_land_map[y][x] == '.':
                copy_land_map[y][x] = '#'
            else:
                copy_land_map[y][x] = '.'
            vertical_mirror, horizontal_mirror = find_mirror_lines(copy_land_map)
            vertical_mirror = vertical_mirror - org_vertical_mirror
            horizontal_mirror = horizontal_mirror - org_horizontal_mirror
            if vertical_mirror or horizontal_mirror:
                sum = 0
                if vertical_mirror:
                    sum += vertical_mirror.pop()
                if horizontal_mirror:
                    sum += horizontal_mirror.pop() * 100
                found_mirrors.append(sum)
        copy_land_map[y] = land_map[y].copy()

    if not found_mirrors:
        raise Exception('No new mirrors found')
    return max(found_mirrors)


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    summary = 0
    for land_map in data:
        pass
        summary += find_corrected_mirror(land_map)
        pass
    return summary


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
