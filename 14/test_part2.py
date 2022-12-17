import pytest
import part2

TEST_INPUT=[
    [(498,4),  (498,6), (496,6)],
    [(503,4),  (502,4), (502,9), (494,9)]
]

def test_test_input():
    with open('test_input2.txt') as testin:
        assert part2.run(testin) == 93

def test_calc_floor():
    assert part2.calc_floor(TEST_INPUT) == 11

