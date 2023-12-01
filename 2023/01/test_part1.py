from part1 import puzzle, parse_input, fiund_calibartion_value

example_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

parsed_input = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]
example_calibration_values = [
    12,
    38,
    15,
    77
]

example_response = 142


def test_example():
    assert puzzle(example_input) == example_response


def test_example_parsing():
    assert parse_input(example_input) == parsed_input


def test_calibration_value():
    for input, value in zip(parsed_input, example_calibration_values):
        assert fiund_calibartion_value(input) == value
