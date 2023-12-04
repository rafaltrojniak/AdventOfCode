import logging
from string import digits

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
from dataclasses import dataclass


def parse_input(input_str: str):
    return input_str.strip().split('\n')


def check_is_symbol(char):
    if char in digits or char in '. \n!':
        return False
    return True


@dataclass(frozen=True)
class Number:
    value: int
    pos_x: int
    pos_y: int


class Engine_map:
    def __init__(self, engine_map):
        self.engine_map = [list(line) for line in engine_map]
        self.numbers_map = {y: {} for y, n in enumerate(engine_map)}
        self.index_numbers()
        self.y_range = range(0, len(engine_map))
        self.x_range = range(0, len(engine_map[0]))

    def index_numbers(self):
        for y, line in enumerate(self.engine_map):
            number = []
            start = None
            for x, char in enumerate(line):
                if char in digits:
                    if not start:
                        start = x
                    number.append(char)
                else:
                    if number:
                        number_obj = Number(
                            value=int(''.join(number)),
                            pos_x=start,
                            pos_y=y
                        )
                        for x in range(start, x):
                            self.numbers_map[y][x] = number_obj
                        number = []
                        start = None

            if number:
                number_obj = Number(
                    value=int(''.join(number)),
                    pos_x=start,
                    pos_y=y
                )
                for x in range(start, x):
                    self.numbers_map[y][x] = number_obj

    def get(self, x, y):
        if x not in self.x_range:
            return '.'
        if y not in self.y_range:
            return '.'
        return self.engine_map[y][x]

    def get_two_adjecent_numbers(self, x: int, y: int) -> int:
        fetched_numbers = [
            self.numbers_map[aim_y].get(aim_x, None)
            for aim_x, aim_y in
            [
                (x + 1, y - 1),
                (x + 1, y),
                (x + 1, y + 1),
                (x, y + 1),
                (x - 1, y + 1),
                (x - 1, y),
                (x - 1, y - 1),
                (x, y - 1)
            ]
        ]
        only_numbers = {number for number in fetched_numbers if number}

        if len(only_numbers) == 2:
            return list(only_numbers)


def puzzle(input_str: str) -> int:
    engine_map = Engine_map(parse_input(input_str))
    total_sum = 0
    for y, line in enumerate(engine_map.engine_map):
        for x, char in enumerate(line):
            if char == '*':
                numbers = engine_map.get_two_adjecent_numbers(x, y)
                if numbers:
                    total_sum += numbers[0].value * numbers[1].value

    return total_sum


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
