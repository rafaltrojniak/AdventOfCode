import pytest
import part1
from io import StringIO

def test_test_input():
    with open('test_input1.txt') as testin:
        assert part1.run(testin) == 'CMZ'

def test_real_input():
    with open('input.txt') as testin:
        assert part1.run(testin) == 'TQRFCBSJJ'

def test_crate_row():
    assert list(part1.read_crate_row('    [D]')) == [None,'D']
def test_crate_row2():
    assert list(part1.read_crate_row('[D]')) == ['D']
def test_crate_row3():
    assert list(part1.read_crate_row('[D]        ')) == ['D',None,None]

def test_read_crates():
    init_stream=StringIO( \
        '    [D]    \n'\
        '[N] [C]    \n'\
        '[Z] [M] [P]\n'\
        ' 1   2   3 \n'
        )

    result={
        1: ['N','Z'],
        2: ['D','C','M'],
        3: ['P']
    }

    assert part1.read_crates(init_stream) == result

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
        3: ['Z','N','D','P']
    }

    assert part1.read_and_exec_moves(init_stream, start) == finish
