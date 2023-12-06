import logging
import re

logger = logging.getLogger()


def parse_input(input_str: str):
    lines = input_str.splitlines()
    times = re.split('\s+', lines[0].split(':')[1].strip())
    dinstances = re.split('\s+', lines[1].split(':')[1].strip())
    return [(int(a), int(b)) for a, b in zip(times, dinstances)]


def calculate_distance(time_push, time_total):
    return (time_total - time_push) * time_push


def puzzle(input_str: str) -> int:
    races = parse_input(input_str)
    result = 1
    for time, record in races:
        test_all_races = [calculate_distance(time_push, time)
                          for time_push in range(1, time)]
        successful_races = filter(lambda x: x > record, test_all_races)
        options = len(list(successful_races))

        result *= options

    return result


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
