import pytest
import part1

def test_test_input():
    with open('test_input1.txt') as testin:
        assert part1.run(testin, row=10) == 26

@pytest.mark.skip
def test_real():
    with open('input.txt') as testin:
        assert part1.run(testin, row=2000000) == 6275922

