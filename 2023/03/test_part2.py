from part2 import puzzle, parse_input

example_input = """467..114..
...*......
..35..633.
......#...
617*......
01...+.58.
..592...10
......755.
...$.*....
.664.598.."""

parsed_input = [
    # 0123456789
    '467..114..',  # 0
    '...*......',  # 1
    '..35..633.',  # 2
    '......#...',  # 3
    '617*......',  # 4
    '01...+.58.',  # 5
    '..592...10',  # 6
    '......755.',  # 7
    '...$.*....',  # 8
    '.664.598..',  # 9
]

example_response = 467835


def test_example_parsing():
    assert parse_input(example_input) == parsed_input


def test_example():
    assert puzzle(example_input) == example_response
