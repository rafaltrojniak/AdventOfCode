from collections import defaultdict


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
    cards = defaultdict(int)
    for number, (winning_bets, my_bets) in enumerate(data):
        cards[number] += 1
        winning_set = set(winning_bets)
        scores = 0
        for bet in my_bets:
            if bet in winning_set:
                scores += 1
        current_card_multiplier = cards[number]
        for won_card_id in range(number + 1, number + scores + 1):
            cards[won_card_id] += current_card_multiplier

    return sum(cards.values())


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
