import re
from math import sqrt, floor


def parse_input(input_str: str):
    lines = input_str.splitlines()
    times = re.split('\s+', lines[0].split(':')[1].strip())
    distances = re.split('\s+', lines[1].split(':')[1].strip())
    return int(''.join(times)), int(''.join(distances))


def puzzle(input_str: str) -> int:
    time, record = parse_input(input_str)

    delta = time * time - 4 * record
    x_right = (time + sqrt(delta)) / 2
    x_left = (time - sqrt(delta)) / 2

    return floor(x_right) - floor(x_left)


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
