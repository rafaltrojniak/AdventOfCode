from part1 import puzzle, parse_input
import pytest

example_input = """Time:      7    15   30
Distance:  9    40  200"""

parsed_input = [
    (7,9),
    (15,40),
    (30,200)
]

example_response = 288

def test_example_parsing():
    assert parse_input(example_input) == parsed_input

def test_example():
    assert puzzle(example_input) == example_response
