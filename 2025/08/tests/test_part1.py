from pathlib import Path

from part1 import puzzle, parse_input
import pytest

example_input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

parsed_input = [
    (162,817,812, 0),
    (57,618,57, 1),
    (906,360,560, 2),
    (592,479,940, 3),
    (352,342,300, 4),
    (466,668,158, 5),
    (542,29,236,  6),
    (431,825,988, 7),
    (739,650,466, 8),
    (52,470,668,  9),
    (216,146,977, 10),
    (819,987,18,  11),
    (117,168,530, 12),
    (805,96,715,  13),
    (346,949,466, 14),
    (970,615,88,  15),
    (941,993,340, 16),
    (862,61,35,   17),
    (984,92,344,  18),
    (425,690,689, 19),
]

example_response = 40

def test_example_parsing():
    assert parse_input(example_input) == parsed_input

def test_example():
    assert puzzle(example_input, 10) == example_response


def test_real_right_response():
    input_path = Path(__file__).resolve().parents[1] / 'input.txt'
    with input_path.open('r') as indata:
        response = puzzle(indata.read(), 1000)
        assert response == 72150
