from part1 import puzzle

#   01234 - x vY
example_input = \
    "7-F7-\n" \
    ".FJ|7\n" \
    "SJLL7\n" \
    "|F--J\n" \
    "LJ.LJ"

parsed_input = []

example_response = 8


# def test_example_parsing():
#    assert parse_input(example_input) == parsed_input

def test_example():
    assert puzzle(example_input) == example_response
