import pytest

from part1 import puzzle, parse_input, find_arragements, verify_arragements

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
    4,
    1,
    1,
    4,
    10,
]

example_response = 21


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
    for arragement, result in zip(parsed_input, possible_arragements):
        assert find_arragements(*arragement) == result


def test_example():
    assert puzzle(example_input) == example_response


@pytest.mark.skip()
def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == 7718
