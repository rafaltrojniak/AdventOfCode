import pytest
import part1

def test_test_input():
    with open('test_input.txt') as testin:
        assert part1.run(testin) == 157

def test_priority_lower():
    assert part1.priority('p')==16

def test_priority_cap():
    assert part1.priority('P')==42
