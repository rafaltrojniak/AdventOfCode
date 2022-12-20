import logging
import re
import itertools
from pprint import pprint
from functools import cache

TIME_AVAILABLE = 26
START_NODE = 'AA'

def generate_dotty(valves, tunnel_map):
    print('digraph abstract{')
    for src, dsts in tunnel_map.items():
        if src in valves:
            print(f'{src} [label="{src}\\n{valves[src]}"];')
        else:
            print(f'{src} [shape=dot,label="{src}"];')
        for dst, weight in dsts.items():
            print(f'{src} -> {dst} [label="{weight}"];')
    print('}')


def read_input(stream):
    valves = {}
    tunnel_map = {}
    for line in stream.readlines():
        #logging.info(line)
        room, rate, tunnels= re.findall(r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]+)", line)[0]
        rate = int(rate)
        tunnels = tunnels.split(', ')
        if rate:
            valves[room] = rate
        tunnel_map[room] = {tunnel:1 for tunnel in tunnels}
    #logging.info(valves)
    #logging.info(tunnel_map)
    return valves, tunnel_map

def reduce_edges(valves, tunnel_map):
    modified = True
    while modified:
        modified = False
        for node, edges in tunnel_map.items():
            if len(edges) == 2 \
                and  node != START_NODE \
                and node not in valves:
                logging.info(f'Found node to reduce - {node} with edges {edges}')
                node_left, node_right  = edges.keys()
                weight_left = edges[node_left]
                weight_right = edges[node_right]
                tunnel_map[node_right][node_left] = tunnel_map[node_left][node]+weight_right
                tunnel_map[node_left][node_right] = tunnel_map[node_right][node]+weight_left
                del tunnel_map[node_right][node]
                del tunnel_map[node_left][node]
                del tunnel_map[node]
                modified=True
                break

def calc_distances(tunnel_map, src_node):
    visited = {}
    look = [(src_node,0)]
    while look:
        node, current_distance= look.pop()
        #logging.info(f'looking at {node}, {current_distance}')
        for candidate, distance in tunnel_map[node].items():
            new_distance = current_distance + distance
            if candidate not in visited \
                or visited[candidate]> new_distance:
                visited[candidate] = new_distance
                look.append((candidate, new_distance))

    return visited

def get_all_distances(tunnel_map):
    distances_graph = {}
    for src_node in tunnel_map.keys():
        for dst_node in tunnel_map.keys():
            if (src_node, dst_node) in distances_graph:
                continue
            for remote_end, distance in calc_distances(tunnel_map, src_node).items():
                if src_node == remote_end:
                    continue
                distances_graph[(src_node, remote_end)] = \
                    distances_graph[(remote_end, src_node)] = distance
    return distances_graph

class Solver:
    def __init__(self, graph, valves):
        self.graph = graph
        self.valves = valves

    @cache
    def find_biggest_presure(self, start, valves_left, time_left):
        current_presure = 0
        if start in self.valves:
            current_presure = self.valves[start] * time_left
        presures = [current_presure ]
        #logging.info(f'analysing from {start} with valves {valves_left} on time {time_left}')
        for end in valves_left:
            distance = self.graph[(start, end)]
            new_time_left = time_left - distance - 1
            if new_time_left > 0 :
                max_presure = self.find_biggest_presure(end, valves_left - {end}, new_time_left)
                presures.append(max_presure + current_presure)
        return max(presures)

    @cache
    def find_biggest_presure_for_second(self, start, valves_left, time_left):
        current_presure = 0
        if start in self.valves:
            current_presure = self.valves[start] * time_left
        presures = [current_presure ]
        presures.append( current_presure  + self.find_biggest_presure( START_NODE, valves_left, TIME_AVAILABLE))
        #logging.info(f'presures combined {presures}')

        #logging.info(f'analysing from {start} with valves {valves_left} on time {time_left}')
        for end in valves_left:
            distance = self.graph[(start, end)]
            new_time_left = time_left - distance - 1
            if new_time_left > 0 :
                max_presure = self.find_biggest_presure_for_second(end, valves_left - {end}, new_time_left)
                presures.append(max_presure + current_presure)
        return max(presures)

def run(stream):
    valves, tunnel_map = read_input(stream)
    reduce_edges(valves, tunnel_map)
    full_graph = get_all_distances(tunnel_map)
    return Solver(full_graph, valves).find_biggest_presure_for_second(START_NODE, frozenset(valves.keys()), TIME_AVAILABLE)

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

