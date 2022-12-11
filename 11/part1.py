import logging
from typing import Union
import re

class Monkey:
    id: int
    work_counter: int
    items: list
    operation: str
    operation_operand: Union[str, int]
    division_factor: int
    target: tuple[int,int]

    def __init__(self, stream):
        #Monkey 0:
        self.id = int(re.findall(r"Monkey (\d+):", stream.readline())[0])
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
        self.work_counter = 0

    def run(self, other_monkeys):
        logging.info(f'Monkey {self.id}:')
        for item in self.items:
            self.work_counter+=1
            logging.info(f'  Monkey inspects an item with a worry level of {item}.')
            if self.operation_operand == 'old':
                operation_operand = item
            else:
                operation_operand = int(self.operation_operand)
            if self.operation == '*':
                item *= operation_operand
                logging.info(f'    Worry level is multiplied by {operation_operand} to {item}.')
            elif self.operation == '+':
                item += operation_operand
                logging.info(f'    Worry level increases by {operation_operand} to {item}.')
            else:
                raise Exception('Unknown operation {self.operation}')
            item =  int(item/3)
            logging.info(f'    Monkey gets bored with item. Worry level is divided by 3 to {item}.')
            if item % self.division_factor:
                logging.info(f'    Current worry level is not divisible by {self.division_factor}.')
                logging.info(f'    Item with worry level {item} is thrown to monkey {self.target[1]}.')
                other_monkeys[self.target[1]].items.append(item)
            else:
                logging.info(f'    Current worry level is divisible by {self.division_factor}.')
                logging.info(f'    Item with worry level {item} is thrown to monkey {self.target[0]}.')
                other_monkeys[self.target[0]].items.append(item)

        self.items = []


def read_monkeys(stream):
    monkeys=[]
    while True:
        monkeys.append(Monkey(stream))
        if not stream.readline():
            break
    return monkeys

def run_round(monkeys):
    for monkey in monkeys:
        monkey.run(monkeys)

def run(stream):
    monkeys = read_monkeys(stream)
    for round_id in range(1, 20+1):
        run_round(monkeys)
    work = [monkey.work_counter for monkey in monkeys]
    work.sort(reverse=True)
    logging.info(work)
    return work[0]*work[1]

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

