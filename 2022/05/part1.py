import logging
import re

def read_crate_row(row:str) -> list:
    while row:
        if len(row)>2 and row[1] and row[1] != ' ':
            yield row[1]
        else:
            yield None
        row = row[4:]

def read_crates(stream):
    storage={}
    while True:
        line = stream.readline()
        if line.startswith(' 1 '):
            return storage
        logging.info(f'parsing line {line}')
        for index, el in enumerate(read_crate_row(line.rstrip())):
            logging.info(f'got item {index} as {el}')
            index+=1
            if el is None:
                continue
            if index in storage:
                storage[index].append(el)
            else:
                storage[index] = [el]

def read_and_exec_moves(stream, crates):
    while True:
        line = stream.readline()
        if not line:
            break
        logging.info(f'move command : {line}')
        amount, src, dst = map(int, re.findall(r"move (\d+) from (\d+) to (\d+)", line)[0])
        while amount>0:
            crates[dst].insert(0, crates[src][0])
            del crates[src][0]
            amount-=1

        logging.info(f'Stack state: {crates}')

    return crates

def run(stream):
    crates = read_crates(stream)
    logging.info(f'crates on init: {crates}')

    '\n' == stream.readline() # Empty line

    crates = read_and_exec_moves(stream,crates)

    towers = list(crates.items())
    towers.sort()
    return ''.join([ tower[0] for index,tower in towers ])

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))
