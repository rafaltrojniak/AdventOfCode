from part2 import puzzle, parse_input, fiund_calibartion_value

example_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

example_calibration_values = [
    29,
    83,
    13,
    24,
    42,
    14,
    76
]

example_response = 281


def test_example():
    assert puzzle(example_input) == example_response


def test_calibration_value():
    for input, value in zip(parse_input(example_input), example_calibration_values):
        assert fiund_calibartion_value(input) == value
