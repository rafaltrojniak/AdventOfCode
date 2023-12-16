import pytest

from part2 import puzzle, parse_input, Contraption, Glass, Point

example_input = \
""".|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""

parsed_input = Contraption(max_x=9,
                           max_y=9,
                           glasses={Point(x=0, y=1): Glass(type='|', orientation=Point(x=1, y=0)),
                                    Point(x=1, y=0): Glass(type='|', orientation=Point(x=1, y=0)),
                                    Point(x=1, y=7): Glass(type='-', orientation=Point(x=0, y=1)),
                                    Point(x=1, y=8): Glass(type='|', orientation=Point(x=1, y=0)),
                                    Point(x=2, y=1): Glass(type='-', orientation=Point(x=0, y=1)),
                                    Point(x=2, y=9): Glass(type='/', orientation=Point(x=-1, y=1)),
                                    Point(x=3, y=7): Glass(type='-', orientation=Point(x=0, y=1)),
                                    Point(x=3, y=9): Glass(type='/', orientation=Point(x=-1, y=1)),
                                    Point(x=4, y=1): Glass(type='\\', orientation=Point(x=1, y=-1)),
                                    Point(x=4, y=6): Glass(type='/', orientation=Point(x=-1, y=1)),
                                    Point(x=4, y=7): Glass(type='/', orientation=Point(x=-1, y=1)),
                                    Point(x=5, y=0): Glass(type='\\', orientation=Point(x=1, y=-1)),
                                    Point(x=5, y=2): Glass(type='|', orientation=Point(x=1, y=0)),
                                    Point(x=5, y=9): Glass(type='|', orientation=Point(x=1, y=0)),
                                    Point(x=6, y=2): Glass(type='-', orientation=Point(x=0, y=1)),
                                    Point(x=6, y=6): Glass(type='\\', orientation=Point(x=1, y=-1)),
                                    Point(x=6, y=8): Glass(type='-', orientation=Point(x=0, y=1)),
                                    Point(x=7, y=6): Glass(type='\\', orientation=Point(x=1, y=-1)),
                                    Point(x=7, y=7): Glass(type='|', orientation=Point(x=1, y=0)),
                                    Point(x=7, y=8): Glass(type='|', orientation=Point(x=1, y=0)),
                                    Point(x=8, y=3): Glass(type='|', orientation=Point(x=1, y=0)),
                                    Point(x=9, y=5): Glass(type='\\', orientation=Point(x=1, y=-1)),
                                    Point(x=9, y=8): Glass(type='\\', orientation=Point(x=1, y=-1))})

example_response = 51


def test_example_parsing():
    assert parse_input(example_input) == parsed_input


def test_example():
    assert puzzle(example_input) == example_response


@pytest.mark.skip()
def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) > 256
