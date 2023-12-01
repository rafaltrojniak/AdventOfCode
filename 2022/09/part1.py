import logging


def run(stream):
    head_x,head_y ,tail_x,tail_y = 0,0,0,0
    tail_positions = set()
    for line in stream.readlines():
        direction, count = line.rstrip().split(' ')
        count=int(count)
        logging.info(f'command {line.strip()}')
        match direction:
            case 'R':
                dx,dy = 1, 0
            case 'L':
                dx,dy = -1, 0
            case 'U':
                dx,dy = 0, -1
            case 'D':
                dx,dy = 0, 1

        for _ in range(0,count):
            old_head_x,old_head_y = head_x,head_y
            head_x += dx
            head_y += dy
            if abs(tail_x - head_x)>1 or abs(tail_y - head_y)>1:
                tail_x,tail_y = old_head_x,old_head_y
            tail_positions.add( (tail_x,tail_y) )
            logging.info(f'head={head_x},{head_y}, tail={tail_x},{tail_y}')
    return len(tail_positions)


if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

