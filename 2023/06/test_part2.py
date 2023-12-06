from part2 import puzzle, parse_input
import pytest

example_input = """Time:      7    15   30
Distance:  9    40  200"""

parsed_input = (
    71530,
    940200

)

example_response = 71503

def test_example_parsing():
    assert parse_input(example_input) == parsed_input

def test_example():
    assert puzzle(example_input) == example_response
