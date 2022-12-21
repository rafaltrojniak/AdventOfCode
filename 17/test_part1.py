import pytest
import part1

def test_test_input():
    with open('test_input1.txt') as testin:
        assert part1.run(testin) == 3068

@pytest.mark.skip
def test_real():
    with open('test_input1.txt') as testin:
        assert part1.run(testin) < 3049

