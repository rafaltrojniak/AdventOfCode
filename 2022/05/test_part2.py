import pytest
import part2
from io import StringIO

def test_test_input():
    with open('test_input2.txt') as testin:
        assert part2.run(testin) == 'MCD'

def test_real_input():
    with open('input.txt') as testin:
        assert part2.run(testin) == 'RMHFJNVFP'

def test_move():
    init_stream=StringIO(
        'move 1 from 2 to 1\n' \
        'move 3 from 1 to 3\n' \
        )
    start={
        1: ['N','Z'],
        2: ['D','C','M'],
        3: ['P']
    }
    finish={
        1: [],
        2: ['C','M'],
        3: ['D','N','Z','P']
    }

    assert part2.read_and_exec_moves(init_stream, start) == finish
