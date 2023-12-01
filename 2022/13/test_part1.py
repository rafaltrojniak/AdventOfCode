import pytest
import part1

RIGHT_INDICES = [1, 2, 4, 6]
RIGHT_INDICES_SUM = 13

def test_test_input_indices():
    with open('test_input1.txt') as testin:
        assert part1.check_messages(testin) == RIGHT_INDICES

def test_test_input():
    with open('test_input1.txt') as testin:
        assert part1.run(testin) == RIGHT_INDICES_SUM

def test_real():
    with open('input.txt') as testin:
        assert part1.run(testin) == 5808

