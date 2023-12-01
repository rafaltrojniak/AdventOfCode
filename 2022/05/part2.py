import logging
import re
import part1

def read_and_exec_moves(stream, crates):
    while True:
        line = stream.readline()
        if not line:
            break
        logging.info(f'move command : {line}')
        amount, src, dst = map(int, re.findall(r"move (\d+) from (\d+) to (\d+)", line)[0])

        crates[dst] = crates[src][0:amount] + crates[dst]
        del crates[src][0:amount]

        logging.info(f'Stack state: {crates}')

    return crates

def run(stream):
    crates = part1.read_crates(stream)
    logging.info(f'crates on init: {crates}')

    '\n' == stream.readline() # Empty line

    crates = read_and_exec_moves(stream,crates)

    towers = list(crates.items())
    towers.sort()
    return ''.join([ tower[0] for index,tower in towers ])

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))
