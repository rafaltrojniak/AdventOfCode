#!/usr/bin/env python
import logging
from dataclasses import dataclass
from collections import deque, defaultdict
from functools import cache
from cProfile import Profile
from pstats import SortKey, Stats

@dataclass(frozen=True)
class Point:
    x: int
    y: int

@dataclass(frozen=True)
class Trip:
    start: Point
    position: Point
    length: int
    visited : frozenset[Point]

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
    graph = defaultdict(set)

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '#':
                continue
            start = Point(x,y)
            for dx, dy in [(0,1), (1,0), (0,-1), (-1, 0)]:
                end=Point(x+dx,y+dy)
                if not (0<end.x < len(data[y]) ) or \
                    not (0<end.y < len(data)):
                    continue
                if data[end.y][end.x] == '#':
                    continue
                pass
                graph[start].add(
                    GraphEdge(
                        start,
                        end,
                        1
                    )
                )
                graph[end].add(
                    GraphEdge(
                        end,
                        start,
                        1
                    )
                )
    return graph

def normalize_graph(graph: dict):

    for key in list(graph.keys()):
        edges:set[GraphEdge] =graph[key]
        if len(edges) == 2:
            new_length = sum([e.length for e in edges])
            points = [e.finish for e in edges]
            for edge in edges:
                old_remote = GraphEdge(start=edge.finish, finish=edge.start, length=edge.length)
                if old_remote not in graph[edge.finish]:
                    pass
                graph[edge.finish].discard(old_remote)
                other_point= [p for p in points if p!= edge.finish][0]
                new_remote = GraphEdge(start=edge.finish, finish=other_point, length=new_length)
                graph[edge.finish].add(new_remote)
            del graph[key]
    return graph


def find_paths(graph, data):

    simplified_graph={
        (key.x, key.y):[
            ((edge.finish.x,edge.finish.y), edge.length)
            for edge in edges
        ]
        for key, edges in graph.items()
    }

    max_y = max([point[1] for point in simplified_graph.keys()])
    end_point = [point for point in simplified_graph.keys() if point[1]==max_y][0]

    def get_max_path( point: tuple, visited: frozenset):
        if point == end_point:
            return 0
        new_visited = frozenset(visited.union([point]))
        lengths=[]
        for next_point, length in simplified_graph[point]:
            if next_point in new_visited:
                continue
            result = get_max_path(next_point, new_visited)
            if result is not None:
                lengths.append(result + length)
        if lengths :
            return max(lengths)

    return get_max_path( (1,0), frozenset())


def find_paths_through_queue(graph, data):
    queue = deque()
    queue.append( (0, Point(1,0), []))

    trips=[]
    best_one=0

    while queue:
        length, point, visited= queue.pop()
        new_visited = visited + [point]
        for edge in graph[point]:
            if edge.finish in new_visited:
                continue

            queue.append( (length+edge.length,
                           edge.finish,
                           new_visited
                           ))
        trips.append(
            (length, point, visited)
        )
    return trips


def print_map(data, nodes, steps):
    nodes=frozenset(nodes)
    for y in range(len(data)):
        for x in range(len(data[y])):
            point = Point(x=x,y=y)
            if point in nodes:
                print('*', end='')
            elif point in steps:
                print('O', end='')
            else:
                print(data[y][x], end='')
        print()


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    graph = generate_graph(data)
#    return graph
    graph = normalize_graph(graph)
    with Profile() as profile:
        max = find_paths(graph, data)
        Stats(profile).strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats()
    return max
    paths = find_paths(graph, data)

    leader = sorted(paths, key=lambda x: x[0])[-1]
    #print_map(data,  leader[1],leader[2])
    #return leader
    return leader[0]


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
