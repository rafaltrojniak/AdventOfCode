import logging
from string import digits

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def parse_input(input_str: str):
    return input_str.strip().split('\n')


def check_is_symbol(char):
    if char in digits or char in '. \n!':
        return False
    return True


class Engine_map:
    def __init__(self, engine_map):
        self.engine_map = [list(line) for line in engine_map]
        self.y_range = range(0, len(engine_map))
        self.x_range = range(0, len(engine_map[0]))

    def get(self, x, y):
        if x not in self.x_range:
            return '.'
        if y not in self.y_range:
            return '.'
        return self.engine_map[y][x]

    def check_is_connected_with_symbol(self, x: int, y: int):
        return any(
            check_is_symbol(self.get(aim_x, aim_y))
            for aim_x, aim_y in [
                (x + 1, y - 1),
                (x + 1, y),
                (x + 1, y + 1),
                (x, y + 1),
                (x - 1, y + 1),
                (x - 1, y),
                (x - 1, y - 1),
                (x, y - 1)
            ]
        )


def puzzle(input_str: str) -> int:
    engine_map = Engine_map(parse_input(input_str))
    total_sum = 0
    for y, line in enumerate(engine_map.engine_map):
        number = []
        is_partnumber = False
        for x, char in enumerate(line):
            if char in digits:
                is_partnumber |= engine_map.check_is_connected_with_symbol(x, y)
                number.append(char)

            else:
                if number and is_partnumber:
                    number = int(''.join(number))
                    total_sum += number
                number = []
                is_partnumber = False
        if number and is_partnumber:
            number = int(''.join(number))
            logger.info(f'found number {number} before {x} and {y}')
            total_sum += number

    return total_sum


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
