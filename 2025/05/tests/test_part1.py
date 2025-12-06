from part1 import puzzle, parse_input
import pytest

example_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

parsed_input = {
    "ranges":[
        range(3,5+1),
        range(10,14+1),
        range(16,20+1),
        range(12,18+1),
    ],
    "ids":[
    1,
    5,
    8,
    11,
    17,
    32
    ]

}

example_response = 3

def test_example_parsing():
    assert parse_input(example_input) == parsed_input

def test_example():
    assert puzzle(example_input) == example_response


def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == 737
