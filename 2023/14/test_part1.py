from part1 import puzzle, parse_input

example_input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

rolled_stones_input = \
    """OOOO.#.O..
    OO..#....#
    OO..O##..O
    O..#.OO...
    ........#.
    ..#....#.#
    ..O..#.O.O
    ..O.......
    #....###..
    #....#...."""

parsed_input = \
    [['O', '.', '.', '.', '.', '#', '.', '.', '.', '.'],
     ['O', '.', 'O', 'O', '#', '.', '.', '.', '.', '#'],
     ['.', '.', '.', '.', '.', '#', '#', '.', '.', '.'],
     ['O', 'O', '.', '#', 'O', '.', '.', '.', '.', 'O'],
     ['.', 'O', '.', '.', '.', '.', '.', 'O', '#', '.'],
     ['O', '.', '#', '.', '.', 'O', '.', '#', '.', '#'],
     ['.', '.', 'O', '.', '.', '#', 'O', '.', '.', 'O'],
     ['.', '.', '.', '.', '.', '.', '.', 'O', '.', '.'],
     ['#', '.', '.', '.', '.', '#', '#', '#', '.', '.'],
     ['#', 'O', 'O', '.', '.', '#', '.', '.', '.', '.']]

example_response = 136


def test_example_parsing():
    assert parse_input(example_input) == parsed_input


def test_example():
    assert puzzle(example_input) == example_response