import logging

NUMBER_OF_KNOTS=10

def print_board(rope, y_range=range(0,5),x_range=range(0,6)):
    print('======')
    for y in reversed(y_range):
        print(f"{y:02d} ",end='')
        for x in x_range:
            if (x,y) in rope:
                index = rope.index((x,y)) or 'H'
                print(index, end='')
            else:
                print('.', end='')
        print()

def run_step(dx,dy,rope):
    new_rope=[(rope[0][0]+dx, rope[0][1]+dy)]
    for knot_id, knot in enumerate(rope):
        if knot_id == 0 :
            continue
        tmp_head = new_rope[knot_id-1]
        ver_distance = tmp_head[0] - knot[0]
        hor_distance = tmp_head[1] - knot[1]
        if abs(ver_distance)>1 or abs(hor_distance)>1:
            # We have lost ocntact, checking what to do
            if ver_distance>0:
                knot=(knot[0]+1,knot[1])
            elif ver_distance<0:
                knot=(knot[0]-1,knot[1])

            if hor_distance>0:
                knot=(knot[0],knot[1]+1)
            elif hor_distance<0:
                knot=(knot[0],knot[1]-1)
        new_rope.append(knot)
    return new_rope

def run(stream):
    rope = [(0,0)]*NUMBER_OF_KNOTS
    tail_positions = set()
    logging.info(f'starting tail positions: {tail_positions}')
    for line in stream.readlines():
        direction, count = line.rstrip().split(' ')
        count=int(count)
        print(f'command {line.strip()}')
        match direction:
            case 'R':
                dx,dy = 1, 0
            case 'L':
                dx,dy = -1, 0
            case 'U':
                dx,dy = 0, +1
            case 'D':
                dx,dy = 0, -1

        for _ in range(0,count):
            new_rope=run_step(dx,dy,rope)
            rope = new_rope
            tail_positions.add(new_rope[-1])
            logging.info(f'head={new_rope[0]}, tail={new_rope[-1]}')
            print_board(rope)
            logging.info(f'tail position: {tail_positions}')
    return len(tail_positions)


if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

