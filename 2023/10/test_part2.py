from part2 import puzzle

#   01234 - x vY
example_input = \
    "FF7FSF7F7F7F7F7F---7\n" \
    "L|LJ||||||||||||F--J\n" \
    "FL-7LJLJ||||||LJL-77\n" \
    "F--JF--7||LJLJ7F7FJ-\n" \
    "L---JF-JLJ.||-FJLJJ7\n" \
    "|F|F-JF---7F7-L7L|7|\n" \
    "|FFJF7L7F-JF7|JL---7\n" \
    "7-L-JL7||F7|L7F-7F7|\n" \
    "L.L7LFJ|||||FJL7||LJ\n" \
    "L7JLJL-JLJLJL--JLJ.L\n"

parsed_input = []

example_response = 10


def test_example():
    assert puzzle(example_input) == example_response


def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == 407
