#!/usr/bin/env python
import logging
import re

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


def puzzle(input_str: str) -> int:
    workflows, gears = parse_input(input_str)

    result_score = 0

    for gear in gears:
        workflow_id = 'in'
        while workflow_id not in ('A', 'R'):
            workflow_id = analyse_gear(workflows[workflow_id], gear)
            logger.info(f'gear {gear=} continued in workflow {workflow_id=}')
        if workflow_id == 'A':
            result_score += sum(gear.values())

    return result_score


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
