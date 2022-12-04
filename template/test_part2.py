import pytest
import part2

def test_test_input():

    with open('test_input2.txt') as testin:
        assert part2.run(testin)

