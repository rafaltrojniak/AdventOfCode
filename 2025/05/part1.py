#!/usr/bin/env python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str):
    ranges = []
    ids = []
    in_ranges = True
    for line in input_str.splitlines():
        if line.strip() == "":
            in_ranges = False
            continue
        if in_ranges:
            start, end = line.split("-")
            ranges.append(range(int(start), int(end) + 1))
        else:
            ids.append(int(line.strip()))
    return {"ranges": ranges, "ids": ids}


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    return sum([any(id_ in r for r in data["ranges"]) for id_ in data["ids"]])


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
