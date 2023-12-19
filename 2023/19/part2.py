#!/usr/bin/env python
import logging
import re
from functools import cache

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str):
    rules = {}
    lines = input_str.strip().splitlines()
    rules_outer = re.compile('([a-z]+)\\{(.*)\\}')
    rule_check = re.compile('(([xmas])([<>])([0-9]*):)?([a-zA-Z]*)')
    while True:
        line = lines.pop(0)
        if not line:
            break
        match = rules_outer.match(line)
        rule_name, rule_checks = match.groups()
        checks = []
        for rule in rule_checks.split(','):
            match = rule_check.match(rule)
            if not match:
                raise Exception(f'Match not found in {rule=}')
            _dummy, check_param, check_function, check_value, action = match.groups()
            if check_param:
                checks.append((check_param, check_function, int(check_value), action))
            else:
                checks.append((action,))

        rules[rule_name] = checks

    parts = []
    while lines:
        line = lines.pop(0)
        if not line:
            break
        gear = {}
        for part in line[1:-1].split(','):
            name, value = part.split('=')
            gear[name] = int(value)
        parts.append(gear)

    return (
        rules,
        parts
    )


def analyse_gear(workflow, gear):
    for check in workflow:
        if len(check) == 1:
            return check[0]
        category, function, value, action = check
        if function == '<' and gear[category] < value:
            return action
        elif function == '>' and gear[category] > value:
            return action


def negate_rule(rule):
    name, function, value = rule
    if function == '<':
        return name, '>', value - 1
    elif function == '>':
        return name, '<', value + 1


def normalise_edges(workflow: list):
    edges = []
    rules = []
    for check in workflow:
        if len(check) == 1:
            edges.append(
                (check[0], tuple(rules))
            )
            continue
        rule = tuple(check[0:3])
        edges.append((check[3], tuple(rules + [rule])))
        rules.append(negate_rule(rule))
    return edges


def render_graphviz(normalised_workflows: dict):
    import graphviz

    g = graphviz.Digraph('G', filename='hello.gv', engine='dot')

    for src, rules in normalised_workflows.items():
        for rule in rules:
            dst, dst_label = rule
            g.edge(head_name=src, tail_name=dst, label=str(dst_label))

    g.view()


@cache
def find_accept_paths(visited: frozenset, org_graph: tuple, head: str):
    graph = dict(org_graph)
    solutions = []
    for node, checks in graph[head]:
        if node == 'R':
            continue
        elif node == 'A':
            solutions.append(checks)
        else:
            retults = find_accept_paths(
                visited=visited.union([head]),
                org_graph=org_graph,
                head=node
            )
            for result in retults:
                solutions.append(
                    checks + result
                )
    return solutions


def agg_rules_into_ranges(rules) -> dict:
    ranges = {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000)
    }
    for name, function, value in rules:
        if function == '<':
            r = ranges[name]
            ranges[name] = (r[0], min(r[1], value - 1))
        elif function == '>':
            r = ranges[name]
            ranges[name] = (max(r[0], value + 1), r[1])
    return ranges


def calc_possibilities(ranges: dict):
    possibilities = 1
    for min, max in ranges.values():
        possibilities *= (max - min + 1)
    return possibilities


def puzzle(input_str: str) -> int:
    workflows, gears = parse_input(input_str)

    normalised_workflows = {
        workflow_id: tuple(normalise_edges(workflow))
        for workflow_id, workflow in workflows.items()
    }

    # render_graphviz(normalised_workflows)

    paths = find_accept_paths(
        visited=frozenset(),
        org_graph=tuple(normalised_workflows.items()),
        head='in'
    )

    ranges = [agg_rules_into_ranges(path) for path in paths]

    return sum([calc_possibilities(range) for range in ranges])


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
