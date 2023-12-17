#!/usr/bin/env python
import logging
from collections import namedtuple
from dataclasses import dataclass
from cProfile import Profile
from pstats import SortKey, Stats

Point = namedtuple('Point', ['x', 'y'])
Beam = namedtuple('Beam', ['point', 'vector'])
Glass = namedtuple('Glass', ['type', 'orientation'])

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


@dataclass
class Contraption:
    max_x: int
    max_y: int
    glasses: dict


def print_contraption(contraption: Contraption, bemas: list[Beam], visited: set):
    beams_vectors_visualization = {
        Point(0, 1): 'v',
        Point(0, -1): '^',
        Point(1, 0): '>',
        Point(-1, 0): '<',

    }
    visited = {b.point: b.vector for b in visited}
    print()
    beams = {beam.point: beam.vector for beam in bemas}
    for y in range(contraption.max_y + 1):
        for x in range(contraption.max_x + 1):
            point = Point(x, y)
            if point in contraption.glasses:
                print(contraption.glasses[point].type, end='')
            elif point in beams:
                print(beams_vectors_visualization[beams[point]], end='')
            elif point in visited:
                print(beams_vectors_visualization[visited[point]], end='')
            else:
                print('.', end='')
        print()


def parse_input(input_str: str):
    data = {}
    for y, line in enumerate(input_str.splitlines()):
        for x, char in enumerate(line):
            point = Point(x, y)
            if char == '|':
                data[point] = Glass('|', Point(1, 0))
            elif char == '-':
                data[point] = Glass('-', Point(0, 1))
            elif char == '\\':
                data[point] = Glass('\\', Point(1, -1))
            elif char == '/':
                data[point] = Glass('/', Point(-1, 1))
    return Contraption(
        max_x=x,
        max_y=y,
        glasses=data
    )


def analyse_beam(contraption: Contraption, beam: Beam):
    beams = {beam}
    visited = set()
    while beams:
        # print_contraption(contraption, beams, visited)
        beam = beams.pop()
        if beam in visited:
            continue
        visited.add(beam)
        new_point = Point(beam.point.x + beam.vector.x, beam.point.y + beam.vector.y)
        if min(new_point.x, new_point.y) < 0 or \
                new_point.y > contraption.max_y or \
                new_point.x > contraption.max_x:
            continue
        if new_point in contraption.glasses:
            glass: Glass = contraption.glasses[new_point]
            if glass.type in '-|':
                if abs(beam.vector.x) == glass.orientation.x \
                        and abs(beam.vector.y) == glass.orientation.y:
                    beams.add(Beam(point=new_point, vector=Point(x=beam.vector.y, y=beam.vector.x)))
                    beams.add(Beam(point=new_point, vector=Point(x=beam.vector.y * -1, y=beam.vector.x * -1)))
                else:
                    beams.add(Beam(point=new_point, vector=beam.vector))
            elif glass.type in '\\':
                beams.add(Beam(point=new_point, vector=Point(x=beam.vector.y, y=beam.vector.x)))
            elif glass.type in '/':
                beams.add(Beam(point=new_point, vector=Point(x=beam.vector.y * -1, y=beam.vector.x * -1)))
        else:
            beams.add(Beam(point=new_point, vector=beam.vector))
    # print_contraption(contraption, beams, visited)
    return len({beam.point for beam in visited}) - 1


def puzzle(input_str: str) -> int:
    contraption = parse_input(input_str)
    return max(
        [analyse_beam(contraption, Beam(Point(x, -1), Point(0, 1)))
         for x in range(0, contraption.max_x + 1)] +
        [analyse_beam(contraption, Beam(Point(x, contraption.max_y + 1), Point(0, -1)))
         for x in range(0, contraption.max_x + 1)] +
        [analyse_beam(contraption, Beam(Point(-1, y), Point(1, 0)))
         for y in range(0, contraption.max_y + 1)] +
        [analyse_beam(contraption, Beam(Point(contraption.max_x + 1, y), Point(-1, 0)))
         for y in range(0, contraption.max_y + 1)]
    )


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        with Profile() as profile:
            print(puzzle(indata.read()))
            Stats(profile).strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats()
