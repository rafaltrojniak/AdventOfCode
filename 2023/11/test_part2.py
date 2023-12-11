from part2 import puzzle, parse_input

example_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

parsed_input = [
    (3, 0),
    (7, 1),
    (0, 2),
    (6, 4),
    (1, 5),
    (9, 6),
    (7, 8),
    (0, 9),
    (4, 9)
]

example_response = 8410


def test_example_parsing():
    assert parse_input(example_input) == parsed_input


def test_example():
    assert puzzle(example_input, expansion_factor=100) == example_response
