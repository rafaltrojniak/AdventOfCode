import pytest
import part1

test_data=[
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
    ('nppdvjthqldpwncqszvftbrmjlhg', 6),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11),
]

def test_test_input():
    for data, position in test_data:
        assert part1.run(data) == position

def test_real_input():
    with open('input.txt') as testin:
        assert part1.run(testin.read()) == 1210
