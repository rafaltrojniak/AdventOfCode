from part2 import puzzle, parse_input
import pytest

example_input = """
"""

parsed_input = []

example_response = 0

def test_example_parsing():
    assert parse_input(example_input) == parsed_input

def test_example():
    assert puzzle(example_input) == example_response
