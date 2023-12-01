import pytest
import part1
import logging

items_started = [
        [79, 98],
        [54, 65, 75, 74],
        [79, 60, 97],
        [74],
    ]

items_after_rouns = {
    1:[
        [20, 23, 27, 26],
        [2080, 25, 167, 207, 401, 1046],
        [],
        [],
    ],
    2:[
        [ 695, 10, 71, 135, 350],
        [ 43, 49, 58, 55, 362],
        [],
        [],
    ],
    3:[
        [ 16, 18, 21, 20, 122],
        [ 1468, 22, 150, 286, 739],
        [ ],
        [ ],
    ],
    4:[
        [ 491, 9, 52, 97, 248, 34],
        [ 39, 45, 43, 258],
        [ ],
        [ ],
    ],
    5:[
        [ 15, 17, 16, 88, 1037],
        [ 20, 110, 205, 524, 72],
        [ ],
        [ ],
    ],
    6:[
        [ 8, 70, 176, 26, 34],
        [ 481, 32, 36, 186, 2190],
        [ ],
        [ ],
    ],
    7:[
        [ 162, 12, 14, 64, 732, 17],
        [ 148, 372, 55, 72],
        [ ],
        [ ],
    ],
    8:[
        [ 51, 126, 20, 26, 136],
        [ 343, 26, 30, 1546, 36],
        [ ],
        [ ],
    ],
    9:[
        [ 116, 10, 12, 517, 14],
        [ 108, 267, 43, 55, 288],
        [ ],
        [ ],
    ],
    10:[
        [ 91, 16, 20, 98],
        [ 481, 245, 22, 26, 1092, 30],
        [ ],
        [ ],
    ],
    15:[
        [ 83, 44, 8, 184, 9, 20, 26, 102],
        [ 110, 36],
        [ ],
        [ ],
    ],
    20:[
        [ 10, 12, 14, 26, 34],
        [ 245, 93, 53, 199, 115],
        [ ],
        [ ],
    ]
}

work_count_after_rounds={
    20: [ 101, 95, 7, 105]
}


def test_items_1_round():
    with open('test_input1.txt') as testin:
        monkeys = part1.read_monkeys(testin)

    assert [list(monkey.items) for monkey in monkeys ] == items_started

    for round_id in range(1,21):
        logging.info(f'Starting round {round_id}')
        part1.run_round(monkeys)
        if round_id in items_after_rouns:
            assert [list(monkey.items) for monkey in monkeys ] ==\
            items_after_rouns[round_id], \
            f'asserting round {round_id}'

        if round_id in work_count_after_rounds:
            assert [monkey.work_counter for monkey in monkeys] ==\
                work_count_after_rounds[round_id ]


def test_test_input():
    with open('test_input1.txt') as testin:
        assert part1.run(testin) == 10605


def test_real():
    with open('input.txt') as testin:
        assert part1.run(testin) == 76728
