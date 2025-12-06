#!/usr/bin/env python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

ADJECENT_VECTORS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1,1)
]


def parse_input(input_str: str):
    map = []
    for line in input_str.strip().splitlines():
        map.append(line)
    return map


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    adjecent_rolls_count_map = sum_adjecent(data)

    rolls_accessibility_map = filter_accessible_rows(adjecent_rolls_count_map, data)

    return sum(
        [
            sum(row)
            for row in rolls_accessibility_map
        ]
    )


def filter_accessible_rows(count: list[list[int]], data: list[str]) -> list[list[bool]]:
    weight_only_on_rolls = [
        [count[x][y] < 4 and data[x][y] == '@' for y in range(len(data[0]))]
        for x in range(len(data))
    ]
    return weight_only_on_rolls


def sum_adjecent(data: list[str]) -> list[list[int]]:
    count = [
        [0] * len(data[0])
        for _ in data
    ]
    x_max = len(data) - 1
    y_max = len(data[0]) - 1
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] == '@':
                for dx,dy in ADJECENT_VECTORS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx <= x_max and 0 <= ny <= y_max:
                        count[nx][ny] += 1
    return count


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
