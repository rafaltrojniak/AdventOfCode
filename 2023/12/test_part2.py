from part2 import puzzle, parse_input, find_arragements, verify_arragements, multiply_data

example_input = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

parsed_input = [
    ('???.###', (1, 1, 3)),
    ('.??..??...?##.', (1, 1, 3)),
    ('?#?#?#?#?#?#?#?', (1, 3, 1, 6)),
    ('????.#...#...', (4, 1, 1)),
    ('????.######..#####.', (1, 6, 5)),
    ('?###????????', (3, 2, 1)),
]

possible_arragements = [
    1,
    16384,
    1,
    16,
    2500,
    506250,
]

example_response = 525152


def test_example_parsing():
    assert parse_input(example_input) == parsed_input


def test_verify_simple_arragements():
    assert verify_arragements('', (1,)) == False
    assert verify_arragements('.', (1,)) == False
    assert verify_arragements('#', (1,)) == True
    assert verify_arragements('..#', (1,)) == True
    assert verify_arragements('..#..', (1,)) == True
    assert verify_arragements('#..', (1,)) == True
    assert verify_arragements('#.#', (1, 1)) == True
    assert verify_arragements('#...#', (1, 1)) == True
    assert verify_arragements('...', (1, 1)) == False
    assert verify_arragements('#..', (1, 1)) == False
    assert verify_arragements('.#.', (1, 1)) == False
    assert verify_arragements('##.', (1, 1)) == False
    assert verify_arragements('..#', (1, 1)) == False
    assert verify_arragements('#.#', (1, 1)) == True
    assert verify_arragements('.##', (1, 1)) == False
    assert verify_arragements('###', (1, 1)) == False


def test_find_simple_arragements():
    assert find_arragements('?', (1,)) == 1
    assert find_arragements('?', (1,)) == 1
    assert find_arragements('?', (2,)) == 0
    assert find_arragements('??', (1, 1)) == 0
    assert find_arragements('??', (1,)) == 2
    assert find_arragements('???', (1,)) == 3
    assert find_arragements('???', (1, 1)) == 1


def test_arragements():
    multiplied_data = multiply_data(parsed_input)
    pass
    assert find_arragements(*multiplied_data[0]) == possible_arragements[0]
    assert find_arragements(*multiplied_data[1]) == possible_arragements[1]
    assert find_arragements(*multiplied_data[2]) == possible_arragements[2]
    assert find_arragements(*multiplied_data[3]) == possible_arragements[3]
    assert find_arragements(*multiplied_data[4]) == possible_arragements[4]
    assert find_arragements(*multiplied_data[5]) == possible_arragements[5]


def test_example():
    assert puzzle(example_input) == example_response
