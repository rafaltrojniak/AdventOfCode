import logging
from functools import cache


ROCKS = [
# ####
    [
        (0,0),(1,0),(2,0),(3,0)
    ],

# .#.
# ###
# .#.
    [ (1,0), (0,1), (1,1), (2,1), (1,2) ],

# ..#
# ..#
# ###
    [ (0,0), (1,0), (2,0), (2,1), (2,2) ],

# #
# #
# #
# #
    [ (0,0), (0,1), (0,2), (0,3)],

# ##
# ##
    [ (0,0), (1,0), (0,1), (1,1)],
]

directions = {
    '<': -1,
    '>': +1,
}

def print_tunnel(tunnel, rock, max_tower):
    logging.info('map: |'+'-'*7)
    for y in reversed(range(0,max_tower+7)):
        line='|'
        for x in range(0,7):
            point = (x,y)
            if point in rock:
                line += '@'
            elif point in tunnel:
                line += '#'
            else:
                line += '.'
        logging.info(f'map: {line}')

def move_rock(rock, direction):
    return [(x+direction,y) for (x,y) in rock]

def fall_rock(rock):
    return [(x,y-1) for (x,y) in rock]

def check_colide(rock, tunnel):
    for (x,y) in rock:
        if (x,y) in tunnel:
            return True
        if x<0 or x>=7:
            return True
    return False

def create_rock(rock, height):
    return [ (x+2, y+height) for x,y in rock]

def check_colide_simplified(rock):
    for (x,y) in rock:
        if x<0 or x>=7:
            return True
    return False

@cache
def calc_fall_for_steps(rock, directions):
    for direction in directions:
        pushed_rock = move_rock(rock, direction)
        if not check_colide_simplified(pushed_rock):
            rock = pushed_rock
        rock = fall_rock(rock)
    return rock


def run(stream, max_rock):
    data = stream.readline().strip()

    wind = [ directions[node] for node in data]

    max_tower = 0

    rock_number = 0
    rock = create_rock(ROCKS[rock_number], max_tower+4)
    rock_position = max_tower + 2

    tunnel = set([(x,0) for x in range(0,7)])
    cycle_limit = 100
    wind_position = 0
    wind_count = len(wind)
    while True:
        #print_tunnel(tunnel, rock, max_tower)
        #cycle_limit -= 1
        #if not cycle_limit:
            #raise Exception('cycle limit hit')

        direction = wind[wind_position % wind_count ]
        wind_position += 1

        pushed_rock = move_rock(rock, direction)
        if not check_colide(pushed_rock, tunnel):
            logging.info('rock push possible')
            rock = pushed_rock
        else:
            logging.info('rock push not possible')

        fallen_rock = fall_rock(rock)
        if not check_colide(fallen_rock, tunnel):
            rock = fallen_rock
        else:
            logging.info('rock fall not possible')
            for (x,y) in rock:
                tunnel.add((x,y))
                max_tower=max(max_tower,y)
            rock_number+=1
            logging.info(f'generating rock {rock_number} with max_tower={max_tower}')
            rock = create_rock(ROCKS[rock_number%len(ROCKS)], max_tower+4)
            # Trying to cache frist position of a rock, but that will not work
            # untill coordinates of the rock would be standarized
            #print_tunnel(tunnel, rock, max_tower)
            #rock = calc_fall_for_steps(tuple(rock),tuple(wind[wind_position:wind_position+1]))
            #print_tunnel(tunnel, rock, max_tower)
            #wind_position += 1

        if rock_number == max_rock:
            return max_tower

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata, 1000000000000))

