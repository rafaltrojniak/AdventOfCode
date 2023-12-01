import pytest
import part2

def test_test_input():
    with open('test_input1.txt') as testin:
        assert part2.run(testin, 2022) == 3068

@pytest.mark.skip
def test_test_input_high_number():
    with open('test_input2.txt') as testin:
        assert part2.run(testin, 1000000000000) == 1514285714288


