#!/usr/bin/env python
import logging
from dataclasses import dataclass
from collections import deque, defaultdict

@dataclass(frozen=True)
class Point:
    x: int
    y: int

@dataclass(frozen=True)
class Trip:
    start: Point
    position: Point
    length: int
    visited : set[Point]

@dataclass(frozen=True)
class GraphEdge:
    start: Point
    finish: Point
    length: int

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str):
    data = []
    for line in input_str.strip().splitlines():
        data.append(list(line))
    return data

DIRECTIONED_SLOPES={
    (0, 1): 'v',
    (0, -1): '^',
    (1, 0): '>',
    (-1, 0): '<',
}

def generate_graph(data):
    queue = deque()
    queue.append(
        Trip(Point(0,0), Point(1,0), 0, set())
    )

    graph = defaultdict(set)

    while queue:
        trip = queue.pop()
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_point = Point(x=trip.position.x+dx, y=trip.position.y+dy)
            if next_point.y == len(data):
                graph[trip.start].add(
                    GraphEdge(
                        start=trip.start,
                        finish=next_point,
                        length=trip.length
                    )
                )
                graph[next_point] = set()
                continue

            next_char = data[next_point.y][next_point.x]
            if next_char == '#':
                continue
            if next_point in trip.visited:
                continue
            if next_char == '.':
                queue.append(
                    Trip(trip.start, next_point,
                         trip.length+1,
                         trip.visited.union(set([trip.position])))
                )
            else:
                if  DIRECTIONED_SLOPES[(dx, dy)] == next_char:
                    # Got the graph node
                    graph[trip.start].add(
                        GraphEdge(
                            start=trip.start,
                            finish=next_point,
                            length=trip.length+1
                        )
                    )
                    queue.append(
                        Trip(next_point, Point(next_point.x+dx, next_point.y+dy),
                             1,
                             set([next_point]))
                    )
    return graph

def normalize_graph(graph: dict):
    normalised_graph = {}
    normalized_edges = set()
    for node, edges in graph.items():
        if node in normalized_edges:
            continue
        if len(edges) != 1:
            normalised_graph[node] = edges
            continue
        [edge] = list(edges)
        while True:
            next_edges = graph[edge.finish]
            if len(next_edges) != 1:
                normalised_graph[node] = set([edge])
                break
            [next_edge] = next_edges
            edge = GraphEdge(
                start=node,
                finish=next_edge.finish,
                length=edge.length + next_edge.length
            )
            normalized_edges.add(next_edge.start)
    return normalised_graph

def find_paths(graph):
    queue = deque()
    queue.append( (0, Point(0,0)))

    trips=[]

    while queue:
        length, point = queue.pop()
        if len(graph[point]):
            for edge in graph[point]:
                queue.append( (length+edge.length, edge.finish))
        else:
            trips.append(length)
    return trips



def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    graph = generate_graph(data)
    graph = normalize_graph(graph)
    paths = find_paths(graph)

    return sorted(paths)[-1]


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
