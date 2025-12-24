#!/usr/bin/env python
import logging
from functools import reduce
from itertools import combinations
from typing import Any

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

# Three dimensional point with an ID
Point = tuple[int, int, int, int]


def parse_input(input_str: str) -> list[Point]:
    points = []
    id = 0  # numbering points for logging
    for line in input_str.strip().splitlines():
        x, y, z = map(int, line.split(","))
        points.append((int(x), int(y), int(z), id))
        id += 1
    return points


def distance(p1: Point, p2: Point) -> int:
    return pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2) + pow(p1[2] - p2[2], 2)


def merge_circuits(circuits: list[Any], p1, p2) -> None:
    circuit1 = None
    circuit2 = None
    for circuit in circuits:
        if p1 in circuit:
            circuit1 = circuit
        if p2 in circuit:
            circuit2 = circuit
    if circuit1 is not None:
        if circuit2 is not None and circuit1 != circuit2:
            logger.info(f"merging circuits {[p[3] for p in circuit1]} and {[p[3] for p in circuit2]}")
            circuit1.update(circuit2)
            circuits.remove(circuit2)
    else:
        raise Exception(f"Not found circuits for missing {p1[3]} {circuit1=} and {p2[3]} {circuit2=}")


def connect_boxes(circuits: list[Any], p1, p2) -> None:
    for circuit in circuits:
        if p2 in circuit:
            logger.info(f"{p1[3]} and {p2[3]} adding to connected {[p[3] for p in circuit]}")
            circuit.add(p1)
            break


def brute_force(data: list[Point], to_connect:int):
    all_directions = [(distance(p1, p2), p1, p2) for p1, p2 in combinations(data, 2)]
    sorted_directions = sorted(all_directions)
    not_used_points = set(data)
    circuits = []
    count = 0
    for dist, p1, p2 in sorted_directions:
        if count == to_connect:
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
        count += 1

    logger.info(f"{circuits=}")
    logger.info([','.join([str(p[3]) for p in circuit]) for circuit in circuits])
    circuit_lengths = [len(circuit) for circuit in circuits]
    sorted_lengths = sorted(circuit_lengths, reverse=True)
    result = reduce(lambda x, y: x * y, sorted_lengths[0:3], 1)
    logger.info(f"{result=}")
    return result


def puzzle(input_str: str, to_connect) -> int:
    data = parse_input(input_str)
    return brute_force(data, to_connect)


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
