from part2 import puzzle, parse_input
import pytest


example_input = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""

parsed_input = [
"123 328  51 64 ",
" 45 64  387 23 ",
"  6 98  215 314",
"*   +   *   +  "
]

example_response = 3263827

def test_example_parsing():
    assert parse_input(example_input) == parsed_input


def test_example():
    assert puzzle(example_input) == example_response

def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == 9630000828442
