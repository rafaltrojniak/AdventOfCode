from part2 import puzzle, parse_input, cycle

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

after_cycle_1 = \
    """.....#....
    ....#...O#
    ...OO##...
    .OO#......
    .....OOO#.
    .O#...O#.#
    ....O#....
    ......OOOO
    #...O###..
    #..OO#...."""

after_cycle_2 = \
    """.....#....
    ....#...O#
    .....##...
    ..O#......
    .....OOO#.
    .O#...O#.#
    ....O#...O
    .......OOO
    #..OO###..
    #.OOO#...O"""

after_cycle_3 = \
    """.....#....
    ....#...O#
    .....##...
    ..O#......
    .....OOO#.
    .O#...O#.#
    ....O#...O
    .......OOO
    #...O###.O
    #.OOO#...O"""

example_response = 64


def test_example():
    assert puzzle(example_input) == example_response


def test_first_cycles():
    rocks_map = parse_input(example_input)
    rocks_map = cycle(rocks_map)
    assert rocks_map == parse_input(after_cycle_1)
    rocks_map = cycle(rocks_map)
    assert rocks_map == parse_input(after_cycle_2)
    rocks_map = cycle(rocks_map)
    assert rocks_map == parse_input(after_cycle_3)
