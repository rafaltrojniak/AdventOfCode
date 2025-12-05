from part1 import puzzle, parse_input

example_input = """987654321111111
811111111111119
234234234234278
818181911112111"""

parsed_input = [
    [9,8,7,6,5,4,3,2,1,1,1,1,1,1,1],
    [8,1,1,1,1,1,1,1,1,1,1,1,1,1,9],
    [2,3,4,2,3,4,2,3,4,2,3,4,2,7,8],
    [8,1,8,1,8,1,9,1,1,1,1,2,1,1,1]
]

example_response = 357

def test_example_parsing():
    assert list(parse_input(example_input)) == parsed_input

def test_example():
    assert puzzle(example_input) == example_response


def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == 17766