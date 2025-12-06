#!/usr/bin/env python
import logging

from part1 import parse_input, sum_adjecent, filter_accessible_rows

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    total = 0
    while True:
        adjecent_roll_count_map = sum_adjecent(data)
        rolls_accessibility_map = filter_accessible_rows(adjecent_roll_count_map, data)
        removed = sum(
            [ sum(row) for row in rolls_accessibility_map ]
        )
        total += removed
        data = remove_rolls_from_data(data, rolls_accessibility_map)
        if removed == 0:
            break
    return total


def remove_rolls_from_data(data: list[str], weight_only_on_rolls: list[bool]) -> list[str]:
    new_data = []
    for x in range(len(data)):
        new_row = ''
        for y in range(len(data[0])):
            if weight_only_on_rolls[x][y]:
                new_row += '.'
            else:
                new_row += data[x][y]
        new_data.append(new_row)
    return new_data


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
