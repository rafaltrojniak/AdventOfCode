WORD_NUMBERS = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
}
REVERSED_WORD_NUMBERS = {
    key[::-1]: value for key, value in WORD_NUMBERS.items()
}


def parse_input(input: str):
    return input.strip().split('\n')


def find_first_occurence(puzzle: str, key_map: dict) -> int:
    while puzzle:
        for key, value in key_map.items():
            if puzzle.startswith(key):
                return value
        puzzle = puzzle[1:]


def fiund_calibartion_value(line: str):
    first = find_first_occurence(line, WORD_NUMBERS)
    last = find_first_occurence(line[::-1], REVERSED_WORD_NUMBERS)
    return int(f'{first}{last}')


def puzzle(input: str) -> int:
    parsed = parse_input(input)
    return sum(map(fiund_calibartion_value, parsed))


if __name__ == "__main__":
    with open('input.txt', 'r') as input_data:
        print(puzzle(input_data.read()))
