from part1 import puzzle, parse_input

example_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

parsed_input = [
('L',68),
('L',30),
('R',48),
('L',5),
('R',60),
('L',55),
('L',1),
('L',99),
('R',14),
('L',82)
]

example_response = 3

def test_example_parsing():
    assert list(parse_input(example_input)) == parsed_input

def test_example():
    assert puzzle(example_input) == example_response


def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == None
