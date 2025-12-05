from part2 import puzzle

from tests.test_part1 import example_input

example_response = 4174379265


def test_example():
    assert puzzle(example_input) == example_response


def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == 40028128307
