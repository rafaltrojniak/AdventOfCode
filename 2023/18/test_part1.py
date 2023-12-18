from part1 import puzzle, parse_input
import pytest

example_input = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

parsed_input = [
    ('R', 6, '70c710'),
    ('D', 5, '0dc571'),
    ('L', 2, '5713f0'),
    ('D', 2, 'd2c081'),
    ('R', 2, '59c680'),
    ('D', 2, '411b91'),
    ('L', 5, '8ceee2'),
    ('U', 2, 'caa173'),
    ('L', 1, '1b58a2'),
    ('U', 2, 'caa171'),
    ('R', 2, '7807d2'),
    ('U', 3, 'a77fa3'),
    ('L', 2, '015232'),
    ('U', 2, '7a21e3'),
]

example_response = 62

def test_example_parsing():
    assert parse_input(example_input) == parsed_input

def test_example():
    assert puzzle(example_input) == example_response



@pytest.mark.skip()
def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == None
