from collections import Counter
from dataclasses import dataclass
from functools import cmp_to_key

CARDS_RANK = {
    digit: rank
    for rank, digit in
    enumerate(reversed('AKQJT98765432'))
}


@dataclass(frozen=True, order=True)
class Hand:
    cards: str
    bid: int

    def rank(self):
        counter = Counter(self.cards)
        counter_values = counter.values()
        if max(counter_values) == 5:
            return 7
        if max(counter_values) == 4:
            return 6
        # Full
        if len(counter_values) == 2 \
                and sorted(counter_values) == [2, 3]:
            return 5
        # Three of a kind
        if len(counter_values) == 3 \
                and sorted(counter_values) == [1, 1, 3]:
            return 4
        # Two pair
        if len(counter_values) == 3 \
                and sorted(counter_values) == [1, 2, 2]:
            return 3
        # One pair
        if len(counter_values) == 4 \
                and sorted(counter_values) == [1, 1, 1, 2]:
            return 2
        # High card
        if len(counter_values) == 5:
            return 1
        raise Exception(f'UnknownRank {self.cards}')


def parse_input(input_str: str):
    hands = []
    for line in input_str.splitlines():
        parts = line.strip().split(' ')
        hands.append(
            Hand(cards=parts[0],
                 bid=int(parts[1])
                 )
        )
    return hands


def compare_hands(x: Hand, y: Hand):
    x_rank = x.rank()
    y_rank = y.rank()
    if x_rank > y_rank:
        return 1
    if x_rank < y_rank:
        return -1
    for x_letter, y_letter in zip(x.cards, y.cards):
        if CARDS_RANK[x_letter] > CARDS_RANK[y_letter]:
            return 1
        if CARDS_RANK[x_letter] < CARDS_RANK[y_letter]:
            return -1
    return 0


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    ordered_hands = sorted(data, key=cmp_to_key(compare_hands))
    return sum([
        hand.bid * rank
        for rank, hand in enumerate(ordered_hands, start=1)
    ])


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
