#!/usr/bin/env python
import logging
import re

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

DECODE_LETTER = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U'
}


def parse_input(input_str: str):
    pattern = re.compile('(.) ([0-9]*) \\(#([a-f0-9]*)\\)')
    matches = [tuple(pattern.match(line).groups()) for line in input_str.strip().splitlines()]

    return [(DECODE_LETTER[color[5]], int(color[0:5], 16)) for letter, depth, color in matches]


DIRECTIONS = {
    'R': (1, 0),
    'L': (-1, 0),
    'D': (0, 1),
    'U': (0, -1),
}


def normalise_ranges(ranges: set) -> set:
    last_range = None
    ranges = sorted(ranges, reverse=True)
    new_ranges = set()
    while ranges:
        new_range = ranges.pop()
        if last_range:
            if last_range[1] == new_range[0]:
                last_range = (last_range[0], new_range[1])
            else:
                new_ranges.add(last_range)
                last_range = new_range
        else:
            last_range = new_range
    if last_range:
        new_ranges.add(last_range)
    return new_ranges


def calc_area(ranges: list, width: int):
    area = 0
    for range_start, range_stop in ranges:
        area += width * (range_stop - range_start + 1)
    return area


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    x, y = (0, 0)
    digs = [(x, y)]
    for direction, length in data:
        dx, dy = DIRECTIONS[direction]
        digs.append((x := x + dx * length, y := y + dy * length, dx, dy))
    # Did we end at start"
    assert digs[-1][0] == digs[-1][1] == 0

    slices = sorted(set([loc[1] for loc in digs]))

    inside_ranges = set()
    last_slice = min(slices) - 1
    area = 0
    for slice in slices:
        # Calc area above
        area += calc_area(inside_ranges, slice - last_slice - 1)

        points = [loc[0] for loc in digs if loc[1] == slice]

        # Let's check if we are within area, or new area

        union_ranges = inside_ranges.copy()

        for new_range in zip(points[0::2], points[1::2]):
            new_start, new_end = min(new_range), max(new_range)
            logger.info(f'{slice=} {new_start=} {new_end=}')
            # Let's check each are if we are within
            for ex_start, ex_end in inside_ranges.copy():
                if new_start >= ex_start and new_end <= ex_end:
                    # We are inside area
                    inside_ranges.remove((ex_start, ex_end))
                    if new_start - ex_start:
                        inside_ranges.add((ex_start, new_start))
                    if ex_end - new_end:
                        inside_ranges.add((new_end, ex_end))
                    break
            else:
                union_ranges.add((new_start, new_end))
                inside_ranges.add((new_start, new_end))

        inside_ranges = normalise_ranges(inside_ranges)
        logger.info(f'{slice=} {sorted(inside_ranges)=}')
        area += calc_area(normalise_ranges(union_ranges), 1)
        logger.info(f'{slice=} {inside_ranges=} {area=}')
        last_slice = slice
    return area


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
