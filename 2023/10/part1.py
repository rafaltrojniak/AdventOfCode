import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

# Direction(x,y)
DIRECTIONS = {
    '|': [(0, 1), (0, -1)],  # is a vertical pipe connecting north and south.
    '-': [(1, 0), (-1, 0)],  # is a horizontal pipe connecting east and west.
    'L': [(0, -1), (1, 0)],  # is a 90-degree bend connecting north and east.
    'J': [(0, -1), (-1, 0)],  # is a 90-degree bend connecting north and west.
    '7': [(-1, 0), (0, 1)],  # is a 90-degree bend connecting south and west.
    'F': [(1, 0), (0, 1)],  # is a 90-degree bend connecting south and east.
    '.': [],  # is ground; there is no pipe in this tile.
    'S': [],
    # is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
}


def parse_input(input_str: str):
    start = None
    graph = {}
    for y, line in enumerate(input_str.strip().splitlines()):
        for x, char in enumerate(line):
            graph[(x, y)] = [
                (x + dx, y + dy)
                for dx, dy in DIRECTIONS[char]
            ]
            if char == 'S':
                start = (x, y)
    start_connections = []
    for address, connected in graph.items():
        if start in connected:
            start_connections.append(address)
    if len(start_connections) != 2:
        raise Exception(f'There should be only two pipes connected to the start, found {start_connections}')

    return graph, start, start_connections


def traverse_graph(graph: dict, last_node: tuple[int, int], node: tuple[int, int]) -> tuple:
    [next_node] = [next_node for next_node in graph[node] if next_node != last_node]
    return next_node


def puzzle(input_str: str) -> int:
    graph, start, start_connections = parse_input(input_str)
    states = [(start, connection, 1) for connection in start_connections]
    wisited = set([start] + start_connections)
    while True:
        new_states = []
        for previous_node, node, steps in states:
            next_node = traverse_graph(graph, previous_node, node)
            new_states.append((node, next_node, steps + 1))
        states = new_states
        new_nodes = [node for _, node, _ in states]
        if any([node in wisited for node in new_nodes]):
            break
        [wisited.add(node) for node in new_nodes]

    return max(steps for _, _, steps in states) - 1


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
