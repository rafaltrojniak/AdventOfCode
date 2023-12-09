from part2 import puzzle, parse_input, find_missing_element

example_input = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

parsed_input = [
    [0, 3, 6, 9, 12, 15],
    [1, 3, 6, 10, 15, 21],
    [10, 13, 16, 21, 30, 45],
]

missing_elements = [
    -3,
    0,
    5,
]

example_response = 2


def test_example_parsing():
    assert parse_input(example_input) == parsed_input


def test_missing_elements():
    for serie, missing_element in zip(parsed_input, missing_elements):
        assert find_missing_element(list(reversed(serie))) == missing_element


def test_example():
    assert puzzle(example_input) == example_response


def test_real_not_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == 1062
