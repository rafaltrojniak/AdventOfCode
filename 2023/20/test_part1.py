import pytest

from part1 import puzzle, parse_input

example_input_1 = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

example_input_2 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

parsed_input_1 = [
    ("broadcaster", "", ('a', 'b', 'c')),
    ("a", "%", ('b',)),
    ("b", "%", ('c',)),
    ("c", "%", ('inv',)),
    ("inv", "&", ('a',)),
]

example_response_1 = 32000000
example_response_2 = 11687500


def test_example_parsing():
    assert parse_input(example_input_1) == parsed_input_1


def test_example1():
    assert puzzle(example_input_1) == example_response_1


def test_example2():
    assert puzzle(example_input_2) == example_response_2


@pytest.mark.skip()
def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == None
