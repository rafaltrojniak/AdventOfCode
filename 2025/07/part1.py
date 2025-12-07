#!/usr/bin/env python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def print_tree(data, beams):
    width = max([x[1] for x in beams]) + 1
    for y in range(data['height']):
        line = ''
        for x in range(width):
            if (y, x) in beams:
                line += '|'
            elif x in data['splitters'][y]:
                line += '^'
            elif (y, x) == data['start']:
                line += 'S'
            else:
                line += '.'
        print(line)


def parse_input(input_str: str):
    lines = {}
    start = None
    for line in input_str.strip().splitlines():
        if 'S' in line:
            start = (len(lines), line.index('S'))

        splitters = set()
        splitter = -1
        try:
            while True:
                splitter = line.index('^', splitter + 1)
                splitters.add(splitter)
        except ValueError:
            pass
        lines[len(lines)] = splitters
    return {"start": start, "height": len(lines), "splitters": lines, }


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    beams = {data['start']}
    all_beams = set()
    split_count = 0
    while beams:
        new_beams = set()
        for y, x in beams:
            # Reached end
            if y + 1 > data['height'] - 1:
                continue
            if x in data['splitters'][y]:
                split_count += 1
                new_beams.add((y + 1, x - 1))
                new_beams.add((y + 1, x + 1))
            else:
                new_beams.add((y + 1, x))
        beams = new_beams
        all_beams = all_beams.union(new_beams)

    # print_tree(data, all_beams)
    return split_count


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
