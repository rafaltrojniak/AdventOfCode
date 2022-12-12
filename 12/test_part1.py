import pytest
import part1

start_elevations=[
    ['a','a','b','q','p','o','n','m'],
    ['a','b','c','r','y','x','x','l'],
    ['a','c','c','s','z','z','x','k'],
    ['a','c','c','t','u','v','w','j'],
    ['a','b','d','e','f','g','h','i'],
]

def test_read_map():
    with open('test_input1.txt') as testin:
        elevations, start, finish = part1.read_map(testin)

    assert start == (0, 0)
    assert finish == (2, 5)
    assert elevations == start_elevations


def test_test_input():
    with open('test_input1.txt') as testin:
        assert part1.run(testin) == 31

@pytest.mark.skip
def test_real():
    with open('input.txt') as testin:
        assert part1.run(testin) == 0
