import pytest

from part2 import puzzle, parse_input, rotate_map, find_corrected_mirror

example_input = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

parsed_input = [
    [
        '#.##..##.',
        '..#.##.#.',
        '##......#',
        '##......#',
        '..#.##.#.',
        '..##..##.',
        '#.#.##.#.',
    ],
    [
        '#...##..#',
        '#....#..#',
        '..##..###',
        '#####.##.',
        '#####.##.',
        '..##..###',
        '#....#..#',
    ]
]

example_response = 400


def test_example_each_map():
    data = parse_input(example_input)
    assert find_corrected_mirror(data[0]) == 300
    assert find_corrected_mirror(data[1]) == 100


def test_example_parsing():
    assert parse_input(example_input) == parsed_input


def test_example():
    assert puzzle(example_input) == example_response


def test_rotate_map():
    assert rotate_map(['A123',
                       'B234',
                       'C345']) == \
           ['ABC',
            '123',
            '234',
            '345']


def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) > 12571


@pytest.mark.skip()
def test_single_mirorr_map():
    mirror_map = [
        '##.####.######.##',
        '.#.#..#.#....#.#.',
        '...#..#...##...#.',
        '###....########..',
        '#..#..#..####..#.',
        '.#.#..#.#.##.#.#.',
        '...####...##...##',
        '..##..##......##.',
        '##.#..#.######.#.',
        '..#....#....#.#..',
        '..#....#......#..',
        '#...##...####...#',
        '#.######.####.###',
        '..##..##......##.',
        '#........####....']
    # assert find_mirror_lines(mirror_map ) == ({5}, set())
    # assert find_mirror_lines(mirror_map ) == ({11,5},set())
    assert find_corrected_mirror(mirror_map) == None
