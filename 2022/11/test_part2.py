import pytest
import part2
import logging

items_started = [
        [79, 98],
        [54, 65, 75, 74],
        [79, 60, 97],
        [74],
    ]

work_count_after_rounds={
    1: [2, 4, 3, 6],
    20: [99, 97, 8, 103],
    1000 : [ 5204 , 4792 , 199 , 5192 ],
    2000 : [ 10419 , 9577 , 392 , 10391 ],
    3000 : [ 15638 , 14358 , 587 , 15593 ],
    4000 : [ 20858 , 19138 , 780 , 20797 ],
    5000 : [ 26075 , 23921 , 974 , 26000 ],
    6000 : [ 31294 , 28702 , 1165 , 31204 ],
    7000 : [ 36508 , 33488 , 1360 , 36400 ],
    8000 : [ 41728 , 38268 , 1553 , 41606 ],
    9000 : [ 46945 , 43051 , 1746 , 46807 ],
    10000 : [ 52166 , 47830 , 1938 , 52013 ],
}


def test_items_rounds():
    with open('test_input1.txt') as testin:
        monkeys = part2.read_monkeys(testin)

    assert [list(monkey.items) for monkey in monkeys ] == items_started

    factors = [monkey.division_factor for monkey in monkeys]
    reduce_factor = 1
    for factor in factors:
        reduce_factor*= factor
    for monkey in monkeys:
        monkey.reduce_factor = reduce_factor

    from pprint import pprint
    print()
    pprint([list(monkey.items) for monkey in monkeys ])


    for round_id in range(1,10000):
        logging.info(f'Starting round {round_id}')
        part2.run_round(monkeys)

        if round_id in work_count_after_rounds:
            assert [monkey.work_counter for monkey in monkeys] ==\
                work_count_after_rounds[round_id ], f'work count after round {round_id}'


#def test_test_input():
#    with open('test_input1.txt') as testin:
#        assert part2.run(testin) == 10605


#def test_real():
#    with open('input.txt') as testin:
#        assert part2.run(testin) == 76728
