import pytest
import part2

def test_test_input():
    with open('test_input2.txt') as testin:
        assert part2.run(testin) == 24933642

def test_real():
    with open('input.txt') as testin:
        assert part2.run(testin)== 12545514

def test_all_size():
    assert part2.get_all_space({'a':1}) == 1
def test_all_size2():
    assert part2.get_all_space({'b':{'a':1}}) == 1
def test_all_size3():
    assert part2.get_all_space({'a':1,'b':2}) == 3
