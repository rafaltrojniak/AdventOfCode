import string


def parse_input(input: str):
    return input.strip().split('\n')


def find_calibartion_value(line: str):
    numbers_in_line = [i for i in line if i in string.digits]
    return int(f'{numbers_in_line[0]}{numbers_in_line[-1]}')


def puzzle(input: str) -> int:
    parsed = parse_input(input)

    return sum(map(find_calibartion_value, parsed))


if __name__ == "__main__":
    with open('input.txt', 'r') as input_data:
        print(puzzle(input_data.read()))
