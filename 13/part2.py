import logging
from functools import cmp_to_key


def read_indices(stream) -> list:
    indices=[]
    while True:
        indices.append(eval(stream.readline()))
        indices.append(eval(stream.readline()))
        if not stream.readline():
            break
    return indices

def check_indices_order(left, right, depth=0)-> bool:
    prefix = '  '*depth
    logging.info(f'{prefix}- Compare {left} vs {right}')
    if type(left) == int and type(right) == int:
        if left>right:
            logging.info(f'{prefix}  - Right side is smaller, so inputs are not in the right order')
            return False
        elif left<right:
            return True
    elif type(left) == list and type(right) == list:
            for left_item ,right_item in zip(left, right):
                match check_indices_order(left_item, right_item, depth+1):
                    case True:
                        return True
                    case False:
                        return False
            if len(left) < len(right):
                logging.info(f'{prefix}- Right side ran out of items, so inputs are not in the right order')
                return True
            if len(left) > len(right):
                logging.info(f'{prefix}- Right side ran out of items, so inputs are not in the right order')
                return False
    elif type(left) == list and type(right) == int:
            right=[right]
            logging.info(f'{prefix}  - Mixed types; convert right to {right} and retry comparison')
            return check_indices_order(left, right, depth+1)
    elif type(left) == int and type(right) == list:
            left=[left]
            logging.info(f'{prefix}  - Mixed types; convert left to {left} and retry comparison')
            return check_indices_order(left, right, depth+1)
    else:
        raise Exception(f'Unexpected conditin - comparing {left} with {right}')
    return None

def map_check_to_comparator(left, right):
    match check_indices_order(left, right):
        case True:
            return 1
        case False:
            return -1
        case None:
            return 0

def sort_packets(packets):
    return sorted(packets, key=cmp_to_key(map_check_to_comparator),
    reverse=True)

DIVIDER_PACKETS=[
    [[2]],
    [[6]]
]


def run(stream):
    packets = read_indices(stream)
    packets += DIVIDER_PACKETS
    packets_sorted = sort_packets(packets)
    key = 1
    for divider in DIVIDER_PACKETS:
        key *= packets_sorted.index(divider)+1
    return key

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

