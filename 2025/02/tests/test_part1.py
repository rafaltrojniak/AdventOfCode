import pytest

from part1 import puzzle, parse_input, is_valid

example_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

parsed_input = [(11, 22), (95, 115), (998, 1012), (1188511880, 1188511890), (222220, 222224), (1698522, 1698528),
    (446443, 446449), (38593856, 38593862), (565653, 565659), (824824821, 824824827), (2121212118, 2121212124), ]

example_response = 1227775554


def test_example_parsing():
    assert list(parse_input(example_input)) == parsed_input


def test_example():
    assert puzzle(example_input) == example_response


def test_real_right_response():
    with open('../input.txt', 'r') as indata:
        assert puzzle(indata.read()) == 28146997880


@pytest.mark.parametrize("value,result",
                         [(11, True), (12, False), (13, False), (22, True), (95, False), (1010, True), (1011, False),
                             (222222, True), (222221, False), ])
def test_valid(value: int, result: bool):
    assert is_valid(value, 2) == result
