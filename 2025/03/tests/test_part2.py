from part2 import puzzle, joltage

from tests.test_part1 import example_input

example_response = 3121910778619


def test_example():
    assert puzzle(example_input) == example_response

def test_joltage():
    assert joltage([1,2,3,4,5,6,7,8,9,0]) == 1234567890

def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == 176582889354075
