import pytest
import part2

def test_test_input():

    with open('test_input2.txt') as testin:
        assert part2.run(testin, x_range=range(0, 20+1), y_range=range(0,20+1)) == 56000011

def test_real():

    with open('input.txt') as testin:
        #assert part2.run(testin, x_range=range(0, 4000000+1), y_range=range(0,4000000+1)) == 11747175442119
        assert part2.run(testin, x_range=range(0, 4000000+1), y_range=range(3442118,4000000+1)) == 11747175442119

