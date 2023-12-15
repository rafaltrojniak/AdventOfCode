from part2 import puzzle, parse_input

example_input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

parsed_input = [
    ("rn", "=", 1),
    ("cm", "-"),
    ("qp", "=", 3),
    ("cm", "=", 2),
    ("qp", "-"),
    ("pc", "=", 4),
    ("ot", "=", 9),
    ("ab", "=", 5),
    ("pc", "-"),
    ("pc", "=", 6),
    ("ot", "=", 7)
]

example_response = 145


def test_example_parsing():
    assert parse_input(example_input) == parsed_input


def test_example():
    assert puzzle(example_input) == example_response
