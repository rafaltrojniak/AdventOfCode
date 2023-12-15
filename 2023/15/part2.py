#!/usr/bin/env python
import logging
from collections import defaultdict
from itertools import starmap

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str):
    orders = []
    for order in input_str.strip().split(','):
        if '=' in order:
            label, number = order.split('=')
            orders.append((label, '=', int(number)))
        elif '-' in order:
            orders.append((order[0:-1], '-'))
    return orders


def hash(src: str) -> int:
    acc = 0
    for char in src:
        acc += ord(char)
        acc = acc * 17 % 256
    return acc


def process_order(box: list, order: tuple):
    if order[1] == '-':
        return [
            el for el in box if el[0] != order[0]
        ]
    elif order[1] == '=':
        new_lens = (order[0], order[2])
        check_label = [el[0] == order[0] for el in box]
        if any(check_label):
            index = check_label.index(True)
            box[index] = new_lens
        else:
            box.append(new_lens)
        return box
    else:
        raise Exception(f'Unknown command type {order=} ')


def calc_power(box_id, box):
    power = 0
    for lens_id, (_lens_name, focus) in enumerate(box, start=1):
        power += lens_id * focus
    return power * (box_id + 1)


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    boxes = defaultdict(list)
    for order in data:
        box_id = hash(order[0])
        boxes[box_id] = process_order(boxes[box_id], order)

    return sum(starmap(calc_power, boxes.items()))


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))