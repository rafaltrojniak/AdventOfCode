import logging

def print_map(stady_sand, rock_map, x_range=range(480, 520), y_range=range(0,12)):
    for y in y_range:
        line = ''
        for x in x_range:
            point=(x,y)
            if point in rock_map:
                line+='#'
            elif point in stady_sand:
                line+='o'
            else:
                line+='.'
        logging.info(f'map: {line}')

def read_input(stream):
    parsed_data = []
    for line in stream.readlines():
        line = line.replace(' -> ','), (')
        data = eval(f'[({line})]')
        parsed_data.append(data)

    return parsed_data
START_SAND = (500, 0)

#
class NoMoveException(Exception):
    pass

#counter=0

def is_possible(sand, stones_map, steady_sand):
#    global counter
#    counter+= 1
#    if counter>1000:
#        raise Exception(f'counter hit, {sand},{rocks}, {steady_sand}')
    #logging.info(f'Checking steady sand {steady_sand}')
    if sand in steady_sand:
        return False

    if sand in stones_map:
        return False
    return True

def calc_next_move(sand, stones_map, steady_sand, floor):
    for dx in (0, -1 , 1):
        new_sand = (sand[0]+dx, sand[1]+1)
        if is_possible(new_sand, stones_map , steady_sand):
            return new_sand

    raise NoMoveException()

def calc_floor(rocks):
    lowest = 0
    for line in rocks:
        for number in range(0, len(line)-1):
            start = line[0]
            end = line[1]
            if not (start[0] == end[0] or  start[1] == end[1]):
                raise Exception(f'(we got not straight line {start} {end}')
        lowest = max(lowest,max([point[1] for point in line]))
    return lowest+2

def calc_map(rocks):
    stones_map = set()
    for line in rocks:
        for number in range(0, len(line)-1):
            start = line[number]
            end = line[number+1]
            x_start = min(start[0],end[0])
            x_end = max(start[0],end[0])
            y_start = min(start[1],end[1])
            y_end = max(start[1],end[1])
            for x in range(x_start,x_end+1):
                for y in range(y_start,y_end+1):
                    stones_map.add((x,y))
    return stones_map

def simulate_sand(rocks):
    steady_sand = set()
    floor = calc_floor(rocks)-1
    stones_map = calc_map(rocks)
    while START_SAND not in steady_sand:
        sand  = START_SAND
        try:
            while True:
                sand = calc_next_move(sand, stones_map, steady_sand, floor)
                if sand[1] == floor:
                    raise NoMoveException()
                #logging.info(f'snad at {sand}')
                #if sand[1] > lowest_rock:
                #    return steady_sand

        except NoMoveException:
            print(f'added sand at {sand}')
            steady_sand.add(sand)
            print_map(steady_sand, stones_map)
    return steady_sand

def run(stream):
    rocks = read_input(stream)
    steady_sand = simulate_sand(rocks)
    return len(steady_sand)

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

