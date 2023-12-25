import pytest

from part2 import puzzle, parse_input



def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == 245114020323037
