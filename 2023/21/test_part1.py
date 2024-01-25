from part1 import puzzle, parse_input, GardenMap, Point
import pytest

example_input = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""

parsed_input = GardenMap(start=Point(x=5, y=5),
          max=Point(x=10, y=10),
          stones=frozenset({Point(x=1, y=2),
                  Point(x=1, y=5),
                  Point(x=1, y=6),
                  Point(x=1, y=8),
                  Point(x=1, y=9),
                  Point(x=2, y=2),
                  Point(x=2, y=3),
                  Point(x=2, y=5),
                  Point(x=2, y=6),
                  Point(x=2, y=8),
                  Point(x=2, y=9),
                  Point(x=3, y=2),
                  Point(x=4, y=3),
                  Point(x=4, y=4),
                  Point(x=4, y=8),
                  Point(x=5, y=1),
                  Point(x=5, y=2),
                  Point(x=5, y=6),
                  Point(x=5, y=9),
                  Point(x=6, y=1),
                  Point(x=6, y=2),
                  Point(x=6, y=4),
                  Point(x=6, y=5),
                  Point(x=6, y=8),
                  Point(x=6, y=9),
                  Point(x=7, y=1),
                  Point(x=7, y=5),
                  Point(x=7, y=7),
                  Point(x=7, y=8),
                  Point(x=8, y=3),
                  Point(x=8, y=5),
                  Point(x=8, y=7),
                  Point(x=8, y=8),
                  Point(x=8, y=9),
                  Point(x=9, y=1),
                  Point(x=9, y=2),
                  Point(x=9, y=5),
                  Point(x=9, y=6),
                  Point(x=9, y=8),
                  Point(x=9, y=9)}))

example_response = 16

def test_example_parsing():
    assert parse_input(example_input) == parsed_input

def test_example():
    assert puzzle(example_input, 6) == example_response


@pytest.mark.skip()
def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == None
