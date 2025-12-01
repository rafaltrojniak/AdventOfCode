from part2 import puzzle, parse_input, analytical_approach, bruteforce_approach
from test_part1 import example_input, parsed_input

example_response = 6

def test_example():
    assert puzzle(example_input) == example_response

def test_real_right_response():
    with open('input.txt', 'r') as indata:
        # 3158 is too low
        value = puzzle(indata.read())
        assert value > 3158
        assert value < 6392
        assert value == 6386


def test_analytical_approach_handles_single_right_move():
    data = [('R', 10)]
    assert analytical_approach(data) == 0

def test_analytical_approach_handles_single_left_move():
    data = [('L', 10)]
    assert analytical_approach(data) == 0

def test_analytical_approach_counts_crossing_zero():
    data = [('L', 60)]
    assert analytical_approach(data) == 1

def test_analytical_approach_counts_multiple_crossings():
    data = [('R', 150)]
    assert analytical_approach(data) == 2

def test_analytical_approach_handles_exact_zero_position():
    data = [('L', 50)]
    assert analytical_approach(data) == 1

def test_analytical_approach_handles_large_rollovers():
    data = [('R', 250)]
    assert analytical_approach(data) == 3

def test_analytical_approach_handles_no_moves():
    data = []
    assert analytical_approach(data) == 0

def test_analytical_approach_handles_large_rollovers():
    data = [('R', 250)]
    assert analytical_approach(data) == 3

def test_rollover_down():
    data = [('R', 40),('L',677)]
    assert analytical_approach(data) == 6

