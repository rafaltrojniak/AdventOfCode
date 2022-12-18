import pytest
import part1

def test_test_input():
    with open('test_input1.txt') as testin:
        assert part1.run(testin, row=10) == 26

