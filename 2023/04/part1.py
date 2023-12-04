def parse_input(input_str: str):
    result = []
    for line in input_str.strip().split('\n'):
        card, numbers = line.split(':')
        winning_numbers, my_numbers = numbers.split('|')
        winning_numbers = winning_numbers.replace('  ', ' ').strip()
        my_numbers = my_numbers.replace('  ', ' ').strip()
        result.append(
            (
                [int(bet) for bet in winning_numbers.split(' ')],
                [int(bet) for bet in my_numbers.split(' ')]
            )
        )
    return result
    pass


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    all_points = 0
    for winning_bets, my_bets in data:
        winning_set = set(winning_bets)
        points = 0
        for bet in my_bets:
            if bet in winning_set:
                if points:
                    points *= 2
                else:
                    points = 1
        all_points += points
    return all_points


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
