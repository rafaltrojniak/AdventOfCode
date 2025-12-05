from part1 import puzzle, parse_input
import pytest

example_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

parsed_input = [
    (11,22),
    (95,115),
    (998,1012),
    (1188511880,1188511890),
    (222220,222224),
    (1698522,1698528),
    (446443,446449),
    (38593856,38593862),
    (565653,565659),
    (824824821,824824827),
    (2121212118,2121212124),
]

example_response = 1227775554

def test_example_parsing():
    assert list(parse_input(example_input)) == parsed_input

def test_example():
    assert puzzle(example_input) == example_response



def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == None
