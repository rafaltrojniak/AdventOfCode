import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str):
    return [
        [int(n) for n in line.strip().split(' ')]
        for line in input_str.strip().splitlines()
    ]


def find_missing_element(sequence: list) -> int:
    deltas = [j - i for i, j in zip(sequence[:-1], sequence[1:])]
    if any(deltas):
        new_delta = find_missing_element(deltas)
    else:
        new_delta = 0
    return sequence[-1] + new_delta


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    logger.info(f'found {len(data)} series')
    missing_elements = list(map(find_missing_element, data))

    return sum(missing_elements)


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
