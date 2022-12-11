import pytest
import part1

items_started = [
        [79, 98],
        [54, 65, 75, 74],
        [79, 60, 97],
        [74],
    ]

items_first_round =  [
    [20, 23, 27, 26],
    [2080, 25, 167, 207, 401, 1046],
    [],
    [],
]

def test_read_items():
    with open('test_input1.txt') as testin:
        assert [list(monkey.items) for monkey in part1.read_monkeys(testin)] == items_started

def test_monkeys_after_first_round():
    pass



def test_test_input():
    with open('test_input1.txt') as testin:
        assert part1.run(testin) == 10605

