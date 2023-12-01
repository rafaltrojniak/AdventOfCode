import pytest
import part1

def test_test_input():
    with open('test_input1.txt') as testin:
        assert part1.run(testin) == 21

def test_test_real():
    with open('input.txt') as testin:
        assert part1.run(testin) == 1713

