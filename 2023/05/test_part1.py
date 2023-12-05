from part1 import puzzle, parse_input, map_locations

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

example_mappings = [
    [79, 81, 81, 81, 74, 78, 78, 82],
    [14, 14, 53, 49, 42, 42, 43, 43],
    [55, 57, 57, 53, 46, 82, 82, 86],
    [13, 13, 52, 41, 34, 34, 35, 35],
]

example_response = 35


def test_example_parsing():
    assert parse_input(example_input) == parsed_input


def test_map_locations():
    resulted_mapping = []
    for locations in example_mappings:
        current_location = locations[0]
        resulting_locations = [current_location]
        for cur_map in parsed_input['maps']:
            current_location = map_locations(current_location, cur_map)
            resulting_locations.append(current_location)
        resulted_mapping.append(resulting_locations)
    assert resulted_mapping == example_mappings


def test_example():
    assert puzzle(example_input) == example_response
