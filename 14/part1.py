import logging

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

def is_possible(sand, rocks, steady_sand):
#    global counter
#    counter+= 1
#    if counter>1000:
#        raise Exception(f'counter hit, {sand},{rocks}, {steady_sand}')
    #logging.info(f'Checking steady sand {steady_sand}')
    if sand in steady_sand:
        return False

    for line in rocks:
        #logging.info(f'Checking line {line}')
        for number in range(0, len(line)-1):
            start = line[number]
            end = line[number+1]
            x_start = min(start[0],end[0])
            x_end = max(start[0],end[0])
            y_start = min(start[1],end[1])
            y_end = max(start[1],end[1])
            #logging.info(f'testing sand {sand} for line {start}-{end}')
            #logging.info(f'test {sand[0]} {range(start[0],end[0]+1)} and {sand[1]} {range(start[1],end[1]+1)}')
            if sand[0] in range(x_start,x_end+1) and sand[1] in range(y_start,y_end+1):
                logging.info(f'Sand is in rock - not possible')
                return False
    return True

def calc_next_move(sand, rocks, steady_sand):
    for dx in (0, -1 , 1):
        new_sand = (sand[0]+dx, sand[1]+1)
        if is_possible(new_sand, rocks, steady_sand):
            return new_sand

    raise NoMoveException()

def calc_lowest_rock(rocks):
    lowest = 0
    for line in rocks:
        for number in range(0, len(line)-1):
            start = line[0]
            end = line[1]
            if not (start[0] == end[0] or  start[1] == end[1]):
                raise Exception(f'(we got not straight line {start} {end}')
        lowest = max(lowest,max([point[1] for point in line]))
    return lowest

def simulate_sand(rocks):
    steady_sand = set()
    lowest_rock = calc_lowest_rock(rocks)
    while True:
        sand  = START_SAND
        try:
            while True:
                sand = calc_next_move(sand, rocks, steady_sand)
                #logging.info(f'snad at {sand}')
                if sand[1] > lowest_rock:
                    return steady_sand

        except NoMoveException:
            print(f'added sand at {sand}')
            steady_sand.add(sand)

def run(stream):
    rocks = read_input(stream)
    steady_sand = simulate_sand(rocks)
    return len(steady_sand)

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

