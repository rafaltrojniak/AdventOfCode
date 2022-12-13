import pytest
import part2

sorted_packets=[
    [],
    [[]],
    [[[]]],
    [1,1,3,1,1],
    [1,1,5,1,1],
    [[1],[2,3,4]],
    [1,[2,[3,[4,[5,6,0]]]],8,9],
    [1,[2,[3,[4,[5,6,7]]]],8,9],
    [[1],4],
    [[2]],
    [3],
    [[4,4],4,4],
    [[4,4],4,4,4],
    [[6]],
    [7,7,7],
    [7,7,7,7],
    [[8,7,6]],
    [9],
]

def test_sorted():
    with open('test_input2.txt') as testin:
        packets = part2.read_indices(testin)
    packets += part2.DIVIDER_PACKETS
    assert part2.sort_packets(packets) == sorted_packets

def test_test_input():
    with open('test_input2.txt') as testin:
        assert part2.run(testin) == 140

def test_real():
    with open('input.txt') as testin:
        assert part2.run(testin) == 22713
