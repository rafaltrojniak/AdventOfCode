import logging
from typing import Union
import re

class Monkey:
    id: int
    items: list
    operation: str
    operation_operand: Union[str, int]
    division_factor: int
    target: tuple[int,int]

    def __init__(self, stream):
        #Monkey 0:
        self.id = map(int, re.findall(r"Monkey (\d+):", stream.readline())[0])
        #  Starting items: 79, 98
        items = re.findall(r"Starting items: ([0-9, ]+)$", stream.readline())[0]
        self.items = list(map(int, items.split(', ')))
        logging.info(f'items: {self.items}')
        #  Operation: new = old * 19
        self.operation, self.operation_operand = \
            re.findall(r"Operation: new = old (.) (old|\d+)$",
            stream.readline())[0]
        logging.info(f'operation: {self.operation} {self.operation_operand}')
        #  Test: divisible by 23
        self.division_factor = \
            int(re.findall(r"Test: divisible by (\d+)$",
           stream.readline())[0])
        logging.info(f'division: {self.division_factor}')

        self.target = [
            int(re.findall(r"If true: throw to monkey (\d+)$",
           stream.readline())[0]),
            int(re.findall(r"If false: throw to monkey (\d+)$",
           stream.readline())[0]),
        ]
        logging.info(f'targets: {self.target}')


def read_monkeys(stream):
    monkeys=[]
    while True:
        monkeys.append(Monkey(stream))
        if not stream.readline():
            break
    return monkeys


def run(stream):
    pass

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

