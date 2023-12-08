import logging
from re import compile


def parse_input(input_str: str):
    input_lines = input_str.splitlines()
    data ={

    }
    data['directions'] = input_lines.pop(0).strip()
    input_lines.pop(0)

    node_regex = compile('(...) = \((...), (...)\)')
    nodes={}
    for line in input_lines:
        match = node_regex.match(line)
        if not match:
            continue
        source, left, right = match.groups()
        nodes[source] = (left, right)
    data['nodes'] = nodes
    return data

def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    steps = 0
    node = 'AAA'
    end_node = 'ZZZ'
    nodes = data['nodes']
    directions = list(data['directions'])
    while node != 'ZZZ':
        direction = directions.pop(0)
        directions = directions+[direction]
        if direction == 'L':
            node = nodes[node][0]
        else:
            node = nodes[node][1]
        steps+=1
    return steps




if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
