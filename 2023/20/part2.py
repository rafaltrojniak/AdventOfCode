#!/usr/bin/env python
import logging
import re
from collections import defaultdict
from collections import deque

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


class FoundSolutionException(Exception):
    pass


def parse_input(input_str: str):
    graph = []
    node_expresion = re.compile('([%&]?)([a-z]+) -> ([a-z ,]+)')
    for line in input_str.strip().splitlines():
        match = node_expresion.fullmatch(line)
        if not match:
            raise Exception(f'Failed parsing of {line=}')
        type, name, destinations = match.groups()
        graph.append(
            (name, type, tuple(destinations.split(', ')))

        )
    return graph


def process_signal(node_type, value, src, state):
    if node_type == '&':
        inputs = dict(state)
        inputs[src] = value
        value = not all(inputs.values())
        return value, tuple(sorted(inputs.items()))
    elif node_type == '%':
        if value == False:
            state = not state
            value = state
            return value, state
        else:
            return None, state


def simulate_signal(graph: dict, states: dict, observe: dict, it: int) -> tuple():
    signals = deque()
    signals.append(("broadcaster", False, "button"))
    edge_states = {}
    while signals:
        node_name, value, src = signals.popleft()
        if src in observe and value:
            observe[src] = it

        if node_name in states:
            signal, new_state = process_signal(graph[node_name][0], value, src, states[node_name])
            states[node_name] = new_state
        else:
            signal = value
        if signal is not None:
            edge_states[node_name] = signal
            for new_dst in graph[node_name][1]:
                signals.append(
                    (new_dst, signal, node_name)
                )

    return states, edge_states


def render_graphviz(graph: list, signals: dict, states: dict):
    import graphviz

    g = graphviz.Digraph('G', filename='hello.gv', engine='dot')

    for src, attrs in graph.items():

        node_type, dsts = attrs

        n_c = 'black'
        if node_type == '%':
            if states[src]:
                n_c = 'green'
            else:
                n_c = 'red'

        g.node(src, f'{node_type}{src}', color=n_c)
        e_c = 'black'

        if src in signals:
            if signals[src]:
                e_c = 'green'
            else:
                e_c = 'red'

        for dst in dsts:
            g.edge(head_name=dst, tail_name=src, color=e_c)

    g.view()


def puzzle(input_str: str, pulses=1000) -> int:
    data = parse_input(input_str)

    # Get reverse graph connections
    reverse_connectoins = defaultdict(set)
    for src, _type, connections in data:
        for dst in connections:
            reverse_connectoins[dst].add(src)

    # Find dummy nodes
    all_src_nodes = set([t[0] for t in data])
    all_dst_nodes = set(reverse_connectoins.keys())
    for node in all_dst_nodes.difference(all_src_nodes):
        data.append(
            (node, "", tuple()),
        )

    # Make sure destinations are in graph

    states = {}
    for node, type, connections in data:
        if type == '%':
            states[node] = False
        elif type == '&':
            # TODO get IDs of sources
            states[node] = tuple([(name, False) for name in reverse_connectoins[node]])

    known_states = set()
    known_state_history = []
    counters = {True: 0, False: 0}

    signals = [
        ('broadcaster', 1)

    ]

    it = 0
    show_iterations = {
        1, 2, 3
    }

    data = {
        name: (node_type, dsts) for name, node_type, dsts in data
    }
    debug = False

    observe = {
        'xr': None,
        'gk': None,
        'gx': None,
        'tf': None
    }

    observe = {
        n: None for n, _x in

        states[list(reverse_connectoins['rx'])[0]]
    }
    try:
        while True:
            if all(observe.values()):
                logger.info(f'found all observes {observe}')
                from math import lcm
                return lcm(*observe.values())
            it += 1
            if it % 100 == 0:
                logger.info(f'got iteration {it}')

            states, edge_signals = simulate_signal(graph=data, states=states, observe=observe, it=it)
    except FoundSolutionException:
        render_graphviz(data, edge_signals, states)
        return it


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
