from part2 import puzzle, parse_input
from test_part1 import example_input, parsed_input

example_response = 6

def test_example():
    assert puzzle(example_input) == example_response

def test_real_right_response():
    with open('input.txt', 'r') as indata:
        # 3158 is too low
        value = puzzle(indata.read())
        assert value > 3158
        assert value < 6392
        assert value == 6386
