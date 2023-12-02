from part1 import puzzle, parse_input

example_input = """
game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

parsed_input = [
    [('blue', 3), ('red', 4), ('red', 1), ('green', 2), ('blue', 6), ('green', 2)],
    [("blue", 1), ("green", 2), ("green", 3), ("blue", 4), ("red", 1),
     ("green", 1), ("blue", 1), ],
    [("green", 8), ("blue", 6), ("red", 20), ("blue", 5), ("red", 4),
     ("green", 13), ("green", 5), ("red", 1), ],
    [("green", 1), ("red", 3), ("blue", 6), ("green", 3), ("red", 6),
     ("green", 3), ("blue", 15), ("red", 14), ],
    [("red", 6), ("blue", 1), ("green", 3), ("blue", 2), ("red", 1),
     ("green", 2), ],

]

example_response = 8


def test_example_parsing():
    assert parse_input(example_input) == parsed_input


def test_example():
    assert puzzle(example_input) == example_response
