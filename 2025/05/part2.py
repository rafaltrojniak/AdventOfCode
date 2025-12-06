#!/usr/bin/env python
import logging

from part1 import parse_input

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    ranges = set(data["ranges"])

    while merge_sets(ranges):
        pass

    return sum(r.stop - r.start for r in ranges)


def merge_sets(ranges: set[range]) -> bool:
    for recipient in ranges:
        for donor in ranges:
            if recipient == donor:
                # We are analysing the same element
                continue
            if recipient.start <= donor.start <= recipient.stop:
                # overlap at start
                new = range(recipient.start, max(recipient.stop, donor.stop))
                ranges.remove(donor)
                ranges.remove(recipient)
                ranges.add(new)
                return True
            if recipient.start <= donor.stop <= recipient.stop:
                # overlap at end
                new = range(min(recipient.start, donor.start), recipient.stop)
                ranges.remove(donor)
                ranges.remove(recipient)
                ranges.add(new)
                return True
    return False


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
