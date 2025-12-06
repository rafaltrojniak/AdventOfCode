from part1 import puzzle, parse_input
import pytest

example_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

parsed_input = [
 '..@@.@@@@.',
 '@@@.@.@.@@',
 '@@@@@.@.@@',
 '@.@@@@..@.',
 '@@.@@@@.@@',
 '.@@@@@@@.@',
 '.@.@.@.@@@',
 '@.@@@.@@@@',
 '.@@@@@@@@.',
 '@.@.@@@.@.']


example_response = 13

def test_example_parsing():
    assert parse_input(example_input) == parsed_input

def test_example():
    assert puzzle(example_input) == example_response


def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == 1409
