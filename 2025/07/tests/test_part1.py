from pathlib import Path

from part1 import puzzle, parse_input
import pytest

example_input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

parsed_input = {
    "start": (0, 7),
    "height": 16,
    "splitters":{
        0: set(),
        1: set(),
        2: {7},
        3: set(),
        4: {6, 8},
        5: set(),
        6: {5, 7, 9},
        7: set(),
        8: {4,6,10},
        9: set(),
        10: {3,5,9,11},
        11: set(),
        12: {2,6,12},
        13: set(),
        14: {1,3,5,7,9,13},
        15: set(),
    }
}

example_response = 21

def test_example_parsing():
    assert parse_input(example_input) == parsed_input

def test_example():
    assert puzzle(example_input) == example_response


def test_real_right_response():
    input_path = Path(__file__).resolve().parents[1] / 'input.txt'
    with input_path.open('r') as indata:
        assert puzzle(indata.read()) == 1711
