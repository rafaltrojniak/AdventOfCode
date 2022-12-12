import logging
import string

def print_map(visited, elevations, finish, look):
    for x in range(0,len(elevations)):
        line=''
        weights=''
        for y in range(0,len(elevations[x])):
            position=(x,y)
            if position == finish:
                line+='F'
                weights+='F'

            elif position in visited:
                (s_x,s_y) , step = visited[position]
                weights+=f'{step%10}'
                if step == 0:
                    line+='S'
                elif s_x > x:
                    line+='v'
                elif s_x < x:
                    line+='^'
                elif s_y > y:
                    line+='>'
                elif s_y < y:
                    line+='<'
                else:
                    line+='.'
            else:
                if position in look:
                    line+='?'
                    weights+='?'
                else:
                    line+=' '
                    weights+=' '
        logging.error(line+' '+weights)


def read_map(stream) :
    elevations=[]
    start = None
    finish = None
    for line in stream.readlines():
        line = list(line.strip())
        if 'S' in line:
            position = line.index('S')
            start=( len(elevations),position)
            line[position] = 'a'
        if 'E' in line:
            position = line.index('E')
            finish=( len(elevations),position)
            line[position] = 'z'
        elevations.append(line)

    logging.info(f'start={start}, finish={finish}')
    return elevations, start, finish



# Check if destination is possible to be moved to
def validate_next(source, destination, elevations):
    x,y = destination
    s_x, s_y = source
    if x<0 or x>=len(elevations) \
        or y<0 or y>=len(elevations[x]) \
        or (ord(elevations[x][y])-ord(elevations[s_x][s_y]))<-1:
        return False
    return True

def run(stream):
    elevations, start, finish = read_map(stream)
    # Key - coordinates (x,y)
    # Value - [(x,y), step], where (x,y) -
    #  source of the move,
    #  step - number of step
    visited={ finish: [ finish, 0]}
    look = [finish]
    it = 10
    while look:
        if len(visited) >= it:
            it += 100
            logging.error(f'iteratoin {it}, visited:{len(visited)}, look:{look}')
            print_map(visited, elevations, finish, look)
#        if it>10000:
#            print_map(visited, elevations, finish, look)
#            raise Exception('Iteration limit exceeded')

        position = look.pop()
        logging.info(f'analysing {position[0]}x{position[1]}')
        _, step = visited[position]
        for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            next_position = (position[0]+dx, position[1]+dy)
            if validate_next(position, next_position, elevations):

                if next_position in visited:
                    _, next_step = visited[next_position]
                    if next_step <= step+1:
                        logging.info(f'Skipping {position[0]}x{position[1]} -> {next_position[0]}x{next_position[1]}, already at step {next_step}, proposed{step+1}')
                        continue
                logging.info(f'{position[0]}x{position[1]} -> {next_position[0]}x{next_position[1]}, {step+1}')
                visited[next_position] = [position, step+1]
                #print_map(visited, elevations, finish, look)
                if next_position not in look:
                    look.append(next_position)

    steps = None
    for x in range(0,len(elevations)):
        for y in range(0,len(elevations)):
            if elevations[x][y]!='a':
                continue
            position=(x,y)
            if position not in visited:
                continue
            _, candidate_steps = visited[position]
            if steps is None or \
                steps > candidate_steps:
                steps= candidate_steps


    return steps


if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

