from part1 import puzzle, parse_input, expand_empty_space, calc_distance

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

expanded_galaxies = [
    (4, 0),
    (9, 1),
    (0, 2),
    (8, 5),
    (1, 6),
    (12, 7),
    (9, 10),
    (0, 11),
    (5, 11)
]

example_response = 374


def test_example_parsing():
    assert parse_input(example_input) == parsed_input


def test_expand_empty_space():
    assert expand_empty_space(parsed_input) == expanded_galaxies


def test_calc_distance():
    assert calc_distance(expanded_galaxies[0], expanded_galaxies[6]) == 15
    assert calc_distance(expanded_galaxies[2], expanded_galaxies[5]) == 17
    assert calc_distance(expanded_galaxies[7], expanded_galaxies[8]) == 5


def test_example():
    assert puzzle(example_input) == example_response
