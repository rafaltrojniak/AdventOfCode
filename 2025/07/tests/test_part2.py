from pathlib import Path

from part2 import puzzle, parse_input
import pytest

from tests.test_part1 import example_input

example_response = 40

def test_example():
    assert puzzle(example_input) == example_response


def test_real_right_response():
    input_path = Path(__file__).resolve().parents[1] / 'input.txt'
    with input_path.open('r') as indata:
        assert puzzle(indata.read()) == 36706966158365
