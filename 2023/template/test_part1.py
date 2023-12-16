from part1 import puzzle, parse_input
import pytest

example_input = """
"""

parsed_input = []

example_response = 0

def test_example_parsing():
    assert parse_input(example_input) == parsed_input

def test_example():
    assert puzzle(example_input) == example_response


@pytest.mark.skip()
def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == None
