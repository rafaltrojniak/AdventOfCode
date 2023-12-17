#!/usr/bin/env python
import logging
from heapq import heappop, heappush

#                    point,         vector,        straight_counter, temperature
# type LawaFlow: tuple[tuple[int,int],tuple[int,int],int, int]

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def parse_input(input_str: str):
    return [list(map(int, line)) for line in input_str.strip().splitlines()]


DIRECTIN_REPRESENTATION = {
    (0, 1): 'v',
    (0, -1): '^',
    (1, 0): '>',
    (-1, 0): '>',
}
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def print_results(heat_map: dict, max_x: int, max_y: int, lava_fronts):
    print()
    lava_fronts = {point: (vector, straight_counter, cost, new_history)
                   for (cost, point, vector, straight_counter, new_history) in lava_fronts
                   }
    for y in range(max_y):
        for x in range(max_x):
            point = (x, y)
            if point in heat_map:
                heat, last, vector, history = heat_map[point]
                print(DIRECTIN_REPRESENTATION[vector], end='')
            else:
                print('.', end='')

        print('  ', end='')
        for x in range(max_x):
            point = (x, y)
            if point in heat_map:
                heat, last, vector, history = heat_map[point]
                print(f'{heat:4}', end='')
            else:
                print(' ...', end='')
        print('  ', end='')
        for x in range(max_x):
            point = (x, y)
            if point in lava_fronts:
                (vector, _straight_counter, _new_cost, _new_history) = lava_fronts[point]
                print(DIRECTIN_REPRESENTATION[vector], end='')
            else:
                print('.', end='')
        print()


def print_history(history, max_x: int, max_y: int):
    history = {point: vector for point, vector, weight in history}
    print()
    for y in range(max_y):
        for x in range(max_x):
            point = (x, y)
            if point in history:
                vector = history[point]
                print(DIRECTIN_REPRESENTATION[vector], end='')
            else:
                print('.', end='')
        print()


def puzzle(input_str: str) -> int:
    heat_loss_map = parse_input(input_str)
    max_y = len(heat_loss_map)
    max_x = len(heat_loss_map[0])
    visited_states = set()
    lava_fronts = []
    heappush(lava_fronts,
             (0, (0, 0), (0, 0), 0, tuple())
             )

    results = []

    while lava_fronts:
        # print_results(visited, max_x, max_y, lava_fronts)

        # Focusing on the front with the lowest heat loss
        temperature, point, vector, straight_counter, history = heappop(lava_fronts)

        state_with_vector = (point, vector, straight_counter)

        if straight_counter == 3:
            continue

        if point[0] == max_x - 1 and point[1] == max_y - 1:
            print_history(history, max_x, max_y)
            return temperature, history

        if state_with_vector in visited_states:
            continue
        visited_states.add(state_with_vector)

        for dx, dy in DIRECTIONS:
            # We are not going back
            if dx * -1 == vector[0] and dy * -1 == vector[1]:
                continue

            next_point = (point[0] + dx, point[1] + dy)
            if not (0 <= next_point[0] < max_x and 0 <= next_point[1] < max_y):
                continue
            new_temperature = temperature + heat_loss_map[next_point[1]][next_point[0]]
            next_vector = (dx, dy)
            if next_vector == vector:
                next_straight_counter = straight_counter + 1
            else:
                next_straight_counter = 0

            next_history = history + ((next_point, next_vector, temperature),)
            heappush(lava_fronts,
                     (new_temperature,
                      next_point, (dx, dy), next_straight_counter, next_history
                      )
                     )


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
