import pytest
import part1
TEST_INPUT=[
    [(498,4),  (498,6), (496,6)],
    [(503,4),  (502,4), (502,9), (494,9)]
]


def test_read_data():
    with open('test_input1.txt') as testin:
        assert part1.read_input(testin) == TEST_INPUT

def test_calc_lowest():
    assert part1.calc_lowest_rock(TEST_INPUT) == 9

def test_possible_rock_horizontal():
    sand = (10,10)
    steady_sand = set()
    rocks = [
        [(9,10),(11,10)]
    ]
    assert part1.is_possible(sand, rocks, steady_sand) == False

def test_possible_rock_horizontal_above():
    sand = (10,0)
    steady_sand = set()
    rocks = [
        [(9,10),(11,10)]
    ]
    assert part1.is_possible(sand, rocks, steady_sand) == True


def test_possible_rock_horizontal_above():
    sand = (10,0)
    steady_sand = set()
    rocks = [
        [(9,10),(11,10)]
    ]
    assert part1.is_possible(sand, rocks, steady_sand) == True

def test_possible_is_steady():
    sand = (10,10)
    steady_sand = set([(10,10)])
    rocks = [ ]
    assert part1.is_possible(sand, rocks, steady_sand) == False


def test_possible_not_steady():
    sand = (10,10)
    steady_sand = set([(11,10)])
    rocks = [ ]
    assert part1.is_possible(sand, rocks, steady_sand) == True

def test_test_input():
   with open('test_input1.txt') as testin:
       assert part1.run(testin) == 24
