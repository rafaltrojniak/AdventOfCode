from part2 import puzzle, parse_input
import pytest

from tests.test_part1 import example_input

example_response = 14

def test_example():
    assert puzzle(example_input) == example_response

def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == 357485433193284
