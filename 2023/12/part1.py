#!/usr/bin/env python
import logging
from collections import Counter
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


@cache
def verify_arragements(spring_map: str, springs: tuple):
    if not springs and not spring_map:
        return True
    if springs and not spring_map:
        return False
    spring_map = list(spring_map)
    my_springs = list(springs)
    if spring_map[0] == '.':
        return verify_arragements(''.join(spring_map[1:]), tuple(springs))
    if not len(springs):
        return False
    elif len(spring_map) < springs[0]:
        return False
    elif spring_map[0:my_springs[0]] == \
            ['#'] * my_springs[0]:
        if len(spring_map) == my_springs[0]:
            if len(my_springs) == 1:
                return True
            else:
                return False
        elif len(spring_map) < my_springs[0] + 1:
            return False
        elif spring_map[my_springs[0]] == '.':
            return verify_arragements(
                ''.join(spring_map[my_springs[0] + 1:]),
                tuple(springs[1:]))
        else:
            return False
    else:
        return False


def genreate_map(spring_map: str, combination: list) -> str:
    local_spring_map = spring_map
    for value in combination:
        local_spring_map = local_spring_map.replace('?', value, 1)
    return local_spring_map


def find_arragements(spring_map: str, springs: tuple) -> int:
    count_chars = Counter(spring_map)
    count = 0
    for combination in product('.#', repeat=count_chars.get('?')):
        test_map = genreate_map(spring_map, combination)
        if verify_arragements(test_map, springs):
            count += 1
    return count


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    return sum(
        [
            find_arragements(*case)
            for case in data
        ]
    )


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
