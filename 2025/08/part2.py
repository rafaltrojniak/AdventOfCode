#!/usr/bin/env python
import logging
from itertools import combinations

from part1 import distance, parse_input, connect_boxes, merge_circuits

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def brute_force(data):
    all_directions = [(distance(p1, p2), p1, p2) for p1, p2 in combinations(data, 2)]
    sorted_directions = sorted(all_directions)
    not_used_points = set(data)
    circuits = []
    last_points = None
    for dist, p1, p2 in sorted_directions:
        if len(circuits) == 1 and not not_used_points:
            break
        if p1 in not_used_points and p2 in not_used_points:
            logger.info(f"{p1[3]} and {p2[3]} are new connection")
            circuits.append({p1, p2})
        elif p1 in not_used_points and p2 not in not_used_points:
            connect_boxes(circuits, p1, p2)
        elif p2 in not_used_points and p1 not in not_used_points:
            connect_boxes(circuits, p2, p1)
        elif p1 not in not_used_points and p2 not in not_used_points:
            merge_circuits(circuits, p1, p2)

        not_used_points.discard(p1)
        not_used_points.discard(p2)
        last_points = (p1, p2)
    logger.info(f"{circuits=}")
    logger.info([','.join([str(p[3]) for p in circuit]) for circuit in circuits])
    return last_points[0][0] * last_points[1][0]


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    return brute_force(data)


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
