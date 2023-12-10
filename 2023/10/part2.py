import logging
from itertools import pairwise

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

LEFT_SIDE_GRADIENT = {
    (0, 1): (1, 0),
    (0, -1): (-1, 0),
    (1, 0): (0, -1),
    (-1, 0): (0, 1)
}
RIGHT_SIDE_GRADIENT = {
    (0, 1): (-1, 0),
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (-1, 0): (0, -1)
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

    return graph, start, start_connections, (x, y)


def traverse_graph(graph: dict, last_node: tuple[int, int], node: tuple[int, int]) -> tuple:
    [next_node] = [next_node for next_node in graph[node] if next_node != last_node]
    return next_node


def find_full_path(graph, start, start_connections):
    path = [start]
    previous_node = start
    node = start_connections[0]
    while node != start:
        path.append(node)
        next_node = traverse_graph(graph, previous_node, node)
        previous_node, node = node, next_node
    path.append(start)
    return path


def get_positions_on_one_side_of_the_path(path: list, gradient: dict):
    path_set = set(path)
    points_on_the_side = set()
    for last_node, next_node in pairwise(path):
        move_gradient = (next_node[0] - last_node[0],
                         next_node[1] - last_node[1])
        side_gradient = gradient[move_gradient]
        side_node = (next_node[0] + side_gradient[0], next_node[1] + side_gradient[1])
        if side_node in path_set:
            continue
        points_on_the_side.add(side_node)
    return points_on_the_side


def expand_on_neighbour_tiles(inside_area_to_check: set[tuple[int, int]], path: list[tuple[int, int]],
                              size: tuple[int, int]):
    path_set = set(path)
    inside_area_checked = inside_area_to_check.copy()
    while inside_area_to_check:
        node = inside_area_to_check.pop()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            candidate = (node[0] + dx, node[1] + dy)
            if candidate in path_set:
                continue
            if candidate in inside_area_checked:
                continue
            inside_area_checked.add(candidate)
            inside_area_to_check.add(candidate)
            if node[0] > size[0] or node[1] > size[1]:
                raise Exception(f'got out of the board at {node=}')
    return inside_area_checked


def puzzle(input_str: str) -> int:
    graph, start, start_connections, size = parse_input(input_str)

    # Get path as a list
    path = find_full_path(graph, start, start_connections)

    inside_area_to_check = get_positions_on_one_side_of_the_path(path, LEFT_SIDE_GRADIENT)
    inside_area_to_check = inside_area_to_check.union(
        get_positions_on_one_side_of_the_path(path[::-1], RIGHT_SIDE_GRADIENT))

    inside_area_checked = expand_on_neighbour_tiles(inside_area_to_check, path, size)

    return len(inside_area_checked)


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
