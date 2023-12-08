import logging
from math import lcm
from re import compile

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str):
    input_lines = input_str.splitlines()

    directions = list(input_lines.pop(0).strip())
    input_lines.pop(0)

    node_regex = compile('(...) = \((...), (...)\)')
    nodes = {}
    for line in input_lines:
        source, left, right = node_regex.match(line).groups()
        nodes[source] = (left, right)

    return directions, nodes


def find_next_stop_for_node(node, directions: list, nodes: dict) -> tuple[str, list, int]:
    steps = 0
    directions = directions.copy()
    while True:
        direction = directions.pop(0)
        directions = directions + [direction]
        if direction == 'L':
            node = nodes[node][0]
        else:
            node = nodes[node][1]
        steps += 1
        if node.endswith('Z'):
            break
    return node, directions, steps


def find_offset_and_cycle(node, directions, nodes) -> tuple[int, int]:
    offset = 0
    old_directions = directions
    while True:
        old_directions = directions
        new_node, directions, more_steps = find_next_stop_for_node(node, directions, nodes)
        if new_node == node and old_directions == directions:
            return offset, more_steps
        else:
            offset += more_steps
            node = new_node


def puzzle(input_str: str) -> int:
    directions, nodes = parse_input(input_str)

    cycles = [
        find_offset_and_cycle(node, directions, nodes)
        for node in nodes.keys()
        if node.endswith('A')
    ]

    # Check if the first trip was the same lenth as offset.
    # This is important as cycle does not end in the start position
    for offset, cycle in cycles:
        if offset != cycle:
            raise Exception('First trip is diferent length than the cycle!')

    # Because all trips are running in cycles, just calculate the minimal time they met
    return lcm(*[cycle for offset, cycle in cycles])


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
