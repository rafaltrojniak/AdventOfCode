#!/usr/bin/env python
import logging
import re
from collections import defaultdict
from collections import deque

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


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


def simulate_signal(graph: tuple, states: tuple) -> tuple():
    graph = {
        name: (node_type, dsts) for name, node_type, dsts in graph
    }
    states = dict(states)
    signal_states = {True: 0, False: 0}

    signals = deque()
    signals.append(("broadcaster", False, "button"))
    while signals:
        node_name, value, src = signals.popleft()
        signal_states[value] += 1
        # logger.info(f'{src} -{value}-> {node_name}')

        if node_name in states:
            signal, new_state = process_signal(graph[node_name][0], value, src, states[node_name])
            states[node_name] = new_state
        else:
            signal = value
        if signal is not None:
            for new_dst in graph[node_name][1]:
                signals.append(
                    (new_dst, signal, node_name)
                )

    return tuple(sorted(states.items())), signal_states


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

    states = []
    for node, type, connections in data:
        if type == '%':
            states.append((node, False))
        elif type == '&':
            # TODO get IDs of sources
            states.append(
                (node,
                 tuple([(name, False) for name in reverse_connectoins[node]])
                 )
            )
    states = tuple(states)

    known_states = set()
    known_state_history = []
    counters = {True: 0, False: 0}

    while True:
        if len(known_states) == pulses:
            break
        states, new_counters = simulate_signal(graph=data, states=states)
        if states in known_states:
            break
        counters = {k: new_counters.get(k, 0) + v for k, v in counters.items()}
        known_states.add(states)

    known_states.add(states)

    all_states = len(known_states)

    cycles = pulses / all_states

    return cycles * cycles * counters[True] * counters[False]


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
