import pytest
import part2

def test_test_input_firstline():
    expected=\
        "##..##..##..##..##..##..##..##..##..##.."

    with open('test_input2.txt') as testin:
        assert part2.run(testin).split('\n')[0] == expected


def test_test_input():
    expected=\
        "##..##..##..##..##..##..##..##..##..##..\n" \
        "###...###...###...###...###...###...###.\n" \
        "####....####....####....####....####....\n" \
        "#####.....#####.....#####.....#####.....\n" \
        "######......######......######......####\n" \
        "#######.......#######.......#######.....\n" \

    with open('test_input2.txt') as testin:
        assert part2.run(testin) == expected


def test_real():
    expected = \
        '####.####..##..####.####.#....#..#.####.\n' \
        '#....#....#..#....#.#....#....#..#.#....\n' \
        '###..###..#......#..###..#....####.###..\n' \
        '#....#....#.....#...#....#....#..#.#....\n' \
        '#....#....#..#.#....#....#....#..#.#....\n' \
        '#....####..##..####.####.####.#..#.####.\n' \


    with open('input.txt') as testin:
        assert part2.run(testin) == expected
