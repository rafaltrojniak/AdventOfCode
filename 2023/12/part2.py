#!/usr/bin/env python
import logging
from functools import cache
from itertools import product

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str):
    result = []
    for line in input_str.strip().splitlines():
        sprint_map, arragements = line.split(' ')
        result.append(
            (
                sprint_map,
                tuple(map(int, arragements.split(',')))

            )
        )
    return result


def replace_with_values(springs_map: str, values: list):
    for value in values:
        springs_map = springs_map.replace('?', value, 1)
    return springs_map


def does_spring_match(spring_map, spring):
    if len(spring_map) < spring:
        return False
    if not set(spring_map[0:spring]).issubset(set('#?')):
        return False
    if len(spring_map) == spring:
        return True
    if spring_map[spring] in '.?':
        return True
    return False


@cache
def find_arragements(spring_map: str, springs: tuple) -> int:
    logger.info(f'analysing {spring_map=} {springs=})')
    if not spring_map and not springs:
        return 1
    if springs and not spring_map:
        return 0
    if spring_map[0] == '.':
        return find_arragements(spring_map[1:], springs)
    if not springs and spring_map:
        if '#' in spring_map:
            return 0
        else:
            return 1
    next_spring = springs[0]
    if spring_map[0] == '?':
        if does_spring_match(spring_map, next_spring):
            return find_arragements(
                spring_map[next_spring + 1:],
                springs[1:]) + \
                find_arragements(spring_map[1:], springs)
        else:
            return find_arragements(spring_map[1:], springs)
    else:
        if does_spring_match(spring_map, next_spring):
            return find_arragements(
                spring_map[next_spring + 1:],
                springs[1:])
        else:
            return 0
    raise Exception('Should not get here')

def multiply_data(data):
    return [
        (
            ('?'.join([springs_map] * 5),
             springs * 5)
        )
        for springs_map, springs in data
    ]


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    multiplied_data = multiply_data(data)
    return sum(
        [
            find_arragements(*case)
            for case in multiplied_data
        ]
    )


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
