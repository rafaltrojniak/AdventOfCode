import pytest
import part2


test_data=[
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb',  19),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz',  23),
    ('nppdvjthqldpwncqszvftbrmjlhg',  23),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',  29),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw',  26),
]

def test_test_input():

    for data, position in test_data:
        assert part2.run(data) == position

def test_real_input():
    with open('input.txt') as testin:
        assert part2.run(testin.read()) == 3476
