from part1 import puzzle, parse_input, rotate_map

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

example_response = 405


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


# @pytest.mark.skip()
def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) > 950
