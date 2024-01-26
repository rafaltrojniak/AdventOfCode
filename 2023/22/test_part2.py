from part2 import puzzle, parse_input, lines_cross
import pytest

example_input = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""

parsed_input = [
 ((1, 0, 1), (1, 2, 1)),
 ((0, 0, 2), (2, 0, 2)),
 ((0, 2, 3), (2, 2, 3)),
 ((0, 0, 4), (0, 2, 4)),
 ((2, 0, 5), (2, 2, 5)),
 ((0, 1, 6), (2, 1, 6)),
 ((1, 1, 8), (1, 1, 9))]

example_response = 7

def test_example_parsing():
    assert parse_input(example_input) == parsed_input

def test_example():
    assert puzzle(example_input) == example_response


@pytest.mark.skip()
def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == 75784


def test_lines_cross():
    assert lines_cross((1,10),(1,1)) == True
    assert lines_cross((1, 10), (2, 2)) == True
    assert lines_cross((2, 2), (1, 10)) == True
    assert lines_cross((2, 20), (1, 10)) == True
    assert lines_cross((2, 2), (2, 10)) == True
    assert lines_cross((10, 20), (3, 10)) == True
    assert lines_cross((2, 2), (3, 10)) == False
    assert lines_cross((20, 20), (3, 10)) == False
