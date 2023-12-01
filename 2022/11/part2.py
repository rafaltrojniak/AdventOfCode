import logging
from typing import Union
import re
import datetime
import gc

class Monkey:
    id: int
    work_counter: int
    items: list
    operation: str
    operation_operand: Union[str, int]
    division_factor: int
    target: tuple[int,int]
    reduce_factor = int

    def __init__(self):
        self.work_counter=0

    def copy(self):
        new_obj  = type(self)()

        new_obj.id= self.id
        new_obj.work_counter= self.work_counter
        new_obj.items= self.items
        new_obj.operation= self.operation
        new_obj.operation_operand=self.operation_operand
        new_obj.division_factor= self.division_factor
        new_obj.target= self.target
        return new_obj

    def read_data(self, stream):
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
        if self.operation_operand == 'old':
            self.operation_operand = None
        else:
            self.operation_operand = int(self.operation_operand)
            logging.info(f'operation: {self.operation} {self.operation_operand}')
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
        self.work_counter += len(self.items)
        for item in self.items:
            logging.info(f'  Monkey inspects an item with a worry level of {item}.')
            if self.operation == '*':
                if self.operation_operand is None:
                    item *= item
                else:
                    item *= self.operation_operand
                logging.info(f'    Worry level is multiplied by {self.operation_operand} to {item}.')
            elif self.operation == '+':
                item +=  self.operation_operand
                logging.info(f'    Worry level increases by {self.operation_operand} to {item}.')

            if item > self.reduce_factor:
                item = item % self.reduce_factor
                logging.info(f'    Reducing the item by {self.reduce_factor} to  {item}.')

            if item % self.division_factor != 0:
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
        monkeys.append(Monkey())
        monkeys[-1].read_data(stream)
        if not stream.readline():
            break
    return monkeys

def run_round(monkeys):
    for monkey in monkeys:
        monkey.run(monkeys)


def run(stream):
    monkeys = read_monkeys(stream)
    factors = [monkey.division_factor for monkey in monkeys]
    reduce_factor = 1
    for factor in factors:
        reduce_factor*= factor
    for monkey in monkeys:
        monkey.reduce_factor = reduce_factor

    for round_id in range(1, 10000+1):
        print(f'round id:{round_id}')
        run_round(monkeys)
    work = [monkey.work_counter for monkey in monkeys]
    work.sort(reverse=True)
    logging.info(work)
    return work[0]*work[1]

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

