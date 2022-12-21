import logging


CHECK_ROCK = 2022

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


def run(stream):
    data = stream.readline().strip()

    wind = [ directions[node] for node in data]

    max_tower = 0

    rock_number = 0
    rock = create_rock(ROCKS[rock_number], max_tower+4)
    rock_position = max_tower + 2

    tunnel = set([(x,0) for x in range(0,7)])
    cycle_limit = 100
    while True:
        for direction in wind:
#            cycle_limit -= 1
#            if not cycle_limit:
#                raise Exception('cycle limit hit')


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
#                print_tunnel(tunnel, rock, max_tower)

            if rock_number == CHECK_ROCK:
                return max_tower

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

