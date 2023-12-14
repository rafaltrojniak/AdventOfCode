#!/usr/bin/env python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str):
    return [list(line) for line in input_str.strip().splitlines()]


def print_rocks(rocks_map):
    print(
        '\n' + '\n'.join([''.join(line) for line in rocks_map])
    )


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    stone_weight = 0
    max_weight = len(data)
    for x in range(0, len(data[0])):
        last_position = 0
        for y in range(0, len(data)):
            if data[y][x] == '#':
                last_position = y + 1
            elif data[y][x] == 'O':
                data[y][x] = '.'
                if data[last_position][x] != '.':
                    raise Exception(f'Rock piled up at {y}{x}')
                stone_weight += max_weight - last_position
                data[last_position][x] = 'O'
                last_position += 1
    print_rocks(data)
    return stone_weight


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
