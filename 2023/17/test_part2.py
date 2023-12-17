import pytest

from part2 import puzzle, parse_input

example_input = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

parsed_input = [
    [2, 4, 1, 3, 4, 3, 2, 3, 1, 1, 3, 2, 3, ],
    [3, 2, 1, 5, 4, 5, 3, 5, 3, 5, 6, 2, 3, ],
    [3, 2, 5, 5, 2, 4, 5, 6, 5, 4, 2, 5, 4, ],
    [3, 4, 4, 6, 5, 8, 5, 8, 4, 5, 4, 5, 2, ],
    [4, 5, 4, 6, 6, 5, 7, 8, 6, 7, 5, 3, 6, ],
    [1, 4, 3, 8, 5, 9, 8, 7, 9, 8, 4, 5, 4, ],
    [4, 4, 5, 7, 8, 7, 6, 9, 8, 7, 7, 6, 6, ],
    [3, 6, 3, 7, 8, 7, 7, 9, 7, 9, 6, 5, 3, ],
    [4, 6, 5, 4, 9, 6, 7, 9, 8, 6, 8, 8, 7, ],
    [4, 5, 6, 4, 6, 7, 9, 9, 8, 6, 4, 5, 3, ],
    [1, 2, 2, 4, 6, 8, 6, 8, 6, 5, 5, 6, 3, ],
    [2, 5, 4, 6, 5, 4, 8, 8, 8, 7, 7, 3, 5, ],
    [4, 3, 2, 2, 6, 7, 4, 6, 5, 5, 5, 3, 3, ],
]

example_response = 94

example2_input = """111111111111
999999999991
999999999991
999999999991
999999999991"""
example2_response = 71


def test_example_parsing():
    assert parse_input(example_input) == parsed_input


def test_example():
    assert puzzle(example_input)[0] == example_response


def test_example2():
    assert puzzle(example2_input)[0] == example2_response


@pytest.mark.skip()
def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read())[0] == 930
