import logging
from itertools import combinations, starmap

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str):
    galaxies = []
    for y, line in enumerate(input_str.strip().splitlines()):
        for x, char in enumerate(line):
            if char == '#':
                galaxies.append((x, y))
    return galaxies


def expand_empty_space(galaxies: list) -> list:
    xes = [g[0] for g in galaxies]
    yes = [g[1] for g in galaxies]
    empty_x = [x for x in range(0, max(xes)) if x not in xes]
    empty_y = [y for y in range(0, max(yes)) if y not in yes]

    new_galaxies = []
    for galaxy in galaxies:
        add_x = sum(map(lambda x: x < galaxy[0], empty_x))
        add_y = sum(map(lambda y: y < galaxy[1], empty_y))
        new_galaxies.append(
            (
                galaxy[0] + add_x,
                galaxy[1] + add_y,
            )
        )
    return new_galaxies


def calc_distance(galaxy1, galaxy2):
    return abs(galaxy1[0] - galaxy2[0]) \
        + abs(galaxy1[1] - galaxy2[1])


def puzzle(input_str: str) -> int:
    galaxies_raw = parse_input(input_str)
    galaxies_expanded = expand_empty_space(galaxies_raw)
    return sum(starmap(calc_distance, combinations(galaxies_expanded, 2)))


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
