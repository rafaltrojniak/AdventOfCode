import pytest
import part2

def test_test_input():
    with open('test_input2.txt') as testin:
        assert part2.run(testin) == 4

def test_range_overlap():
    assert part2.check_overlap('1-10,2-3') == True
def test_range_overlap2():
    assert part2.check_overlap('2-3,1-10') == True

def test_range_touch():
    assert part2.check_overlap('0-6,6-10') == True
def test_range_touch2():
    assert part2.check_overlap('6-10,0-6') == True
def test_range_separate():
    assert part2.check_overlap('0-5,6-10') == False
def test_range_separate2():
    assert part2.check_overlap('6-10,0-5') == False

