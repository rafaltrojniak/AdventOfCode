import pytest
import part1

def test_test_input():
    with open('test_input1.txt') as testin:
        assert part1.run(testin) == 2

def test_range_overlap():
    assert part1.check_overlap('0-10,1-2') == True

def test_range_separate():
    assert part1.check_overlap('0-5,6-10') == False
