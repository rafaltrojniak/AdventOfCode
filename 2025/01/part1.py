#!/usr/bin/env python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str):
    for line in input_str.splitlines():
        dir = line[0]
        amount=int(line[1:])
        yield (dir, amount)

def puzzle(input_str: str) -> int:
    data = list(parse_input(input_str))
    count=0
    position=50
    for dir, amount in data:
        position +=100
        if dir == 'R':
            position+=amount
        else:
            position-=amount
        position%=100
        if not position:
            count+=1
    return count



    pass


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
