import logging

def check_visible(x,y,trees):
    height = trees[x][y]
    # Check up
    score_x_up=0
    x_up=x
    while x_up != 0:
        x_up=x_up-1
        score_x_up+=1
        if trees[x_up][y]>=height:
            break

    score_x_down=0
    x_down=x
    while x_down != len(trees)-1:
        x_down=x_down+1
        score_x_down+=1
        if trees[x_down][y]>=height:
            break

    score_y_up=0
    y_up=y
    while y_up != 0:
        y_up=y_up-1
        score_y_up+=1
        if trees[x][y_up]>=height:
            break

    score_y_down=0
    y_down=y
    while y_down != len(trees[0])-1:
        y_down=y_down+1
        score_y_down+=1
        if trees[x][y_down]>=height:
            break
    logging.info(f'scores: {score_x_up} {score_x_down} {score_y_up} {score_y_down}')
    return \
        score_x_up*score_x_down *\
        score_y_up*score_y_down

def run(stream):
    trees=[]
    for row in stream.readlines():
        row = list(map(int, row.strip()))
        logging.info(f'added row:{row}')
        trees.append(row)

    scores=[]
    for x in range(0,len(trees)):
        row=[]
        for y in range(0,len(trees[0])):
            row.append(check_visible(x,y,trees))
        logging.info(f'visibility :{row}')
        scores.append(max(row))

    return max(scores)

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

