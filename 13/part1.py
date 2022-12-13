import logging

def read_indices(stream) -> list:
    indices=[]
    while True:
        left = eval(stream.readline())
        right = eval(stream.readline())
        indices.append( (left, right) )
        if not stream.readline():
            break
    return indices

def check_indices_order(indices_pair, depth=0)-> bool:
    left, right = indices_pair
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
                match check_indices_order((left_item, right_item), depth+1):
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
            return check_indices_order((left, right), depth+1)
    elif type(left) == int and type(right) == list:
            left=[left]
            logging.info(f'{prefix}  - Mixed types; convert left to {left} and retry comparison')
            return check_indices_order((left, right), depth+1)
    else:
        raise Exception(f'Unexpected conditin - comparing {left} with {right}')
    return None

def check_messages(stream) -> list:
    indices = read_indices(stream)
    ordered_ids=[]
    for pair_id, pair in enumerate(indices, start=1):
        logging.info(f'== Pair {pair_id} ==')
        if check_indices_order(pair):
            ordered_ids.append(pair_id)
        logging.info('')
    return ordered_ids


def run(stream):
    return sum( check_messages(stream))

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

