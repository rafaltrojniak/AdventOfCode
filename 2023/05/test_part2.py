from part2 import puzzle, parse_input, model_ranges, check_ranges_intersect, map_ranges

with open('test_input1.txt', 'r') as testin_fd:
    example_input = testin_fd.read()

parsed_input = {
    'seeds': [79, 14, 55, 13],
    'maps': [
        [
            [50, 98, 2],
            [52, 50, 48],
        ],
        [
            [0, 15, 37],
            [37, 52, 2],
            [39, 0, 15],
        ],
        [
            [49, 53, 8],
            [0, 11, 42],
            [42, 0, 7],
            [57, 7, 4],
        ],
        [
            [88, 18, 7],
            [18, 25, 70],
        ],
        [
            [45, 77, 23],
            [81, 45, 19],
            [68, 64, 13],
        ],
        [
            [0, 69, 1],
            [1, 0, 69],
        ],
        [
            [60, 56, 37],
            [56, 93, 4],
        ],
    ]

}

example_parsed_ranges = {
    'seeds': [range(79, 93), range(55, 68)],
    'maps': [
        [(range(98, 100), range(50, 52)),
         (range(50, 98), range(52, 100))],
        [(range(15, 52), range(0, 37)),
         (range(52, 54), range(37, 39)),
         (range(0, 15), range(39, 54))],
        [(range(53, 61), range(49, 57)),
         (range(11, 53), range(0, 42)),
         (range(0, 7), range(42, 49)),
         (range(7, 11), range(57, 61))],
        [(range(18, 25), range(88, 95)), (range(25, 95), range(18, 88))],
        [(range(77, 100), range(45, 68)),
         (range(45, 64), range(81, 100)),
         (range(64, 77), range(68, 81))],
        [(range(69, 70), range(0, 1)), (range(0, 69), range(1, 70))],
        [(range(56, 93), range(60, 97)), (range(93, 97), range(56, 60))]
    ]

}

example_response = 46


def test_example_parsing():
    assert parse_input(example_input) == parsed_input


def test_model_ranges():
    assert model_ranges(parsed_input) == example_parsed_ranges


def test_ranges_intersect():
    assert check_ranges_intersect(range(0, 1), range(1, 2)) == False
    assert check_ranges_intersect(range(1, 2), range(0, 1)) == False
    assert check_ranges_intersect(range(1, 10), range(2, 3)) == True
    assert check_ranges_intersect(range(1, 10), range(1, 3)) == True
    assert check_ranges_intersect(range(1, 10), range(5, 10)) == True
    assert check_ranges_intersect(range(1, 10), range(5, 9)) == True
    assert check_ranges_intersect(range(1, 10), range(5, 12)) == True
    assert check_ranges_intersect(range(2, 10), range(0, 5)) == True


def test_process_ranges():
    assert map_ranges(range(0, 10), range(0, 10), range(20, 30)) == (range(20, 30), [])
    assert map_ranges(range(0, 100), range(10, 20), range(20, 30)) == (range(20, 30), [range(0, 10), range(20, 100)])


def test_example():
    assert puzzle(example_input) == example_response
