from functools import cmp_to_key

from part1 import puzzle, parse_input, Hand, compare_hands

example_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483 """

parsed_input = [
    Hand('32T3K', 765),
    Hand('T55J5', 684),
    Hand('KK677', 28),
    Hand('KTJJT', 220),
    Hand('QQQJA', 483),
]

hands_ordered = [
    Hand('32T3K', 765),  # 1
    Hand('KTJJT', 220),  # 2
    Hand('KK677', 28),  # 3
    Hand('T55J5', 684),  # 4
    Hand('QQQJA', 483),  # 5
]

example_response = 6440


def test_example_parsing():
    assert parse_input(example_input) == parsed_input


def test_sorting():
    assert sorted(parsed_input, key=cmp_to_key(compare_hands)) == hands_ordered


def test_example():
    assert puzzle(example_input) == example_response
