import logging

def check_visible(x,y,trees):
    height = trees[x][y]
    # Check up
    x_up=x
    height_up=height
    condition=True
    while x_up != 0:
        x_up=x_up-1
        if not trees[x_up][y]<height:
            condition=False
            break
        height_up = trees[x_up][y]
    if condition:
        return True
    x_down=x
    height_down=height
    condition=True
    while x_down != len(trees)-1:
        x_down=x_down+1
        if not trees[x_down][y]<height:
            condition=False
            break
        height_down = trees[x_down][y]
    if condition:
        return True
    y_up=y
    height_up=height
    condition=True
    while y_up != 0:
        y_up=y_up-1
        if not trees[x][y_up]<height:
            condition=False
            break
        height_up = trees[x][y_up]
    if condition:
        return True
    y_down=y
    height_down=height
    condition=True
    while y_down != len(trees[0])-1:
        y_down=y_down+1
        if not trees[x][y_down]<height:
            condition=False
            break
        height_down = trees[x][y_down]
    if condition:
        return True
    return False

def run(stream):
    trees=[]
    for row in stream.readlines():
        row = list(map(int, row.strip()))
        logging.info(f'added row:{row}')
        trees.append(row)

    visible = []
    visible_sum=0
    for x in range(0,len(trees)):
        visible.append([])
        for y in range(0,len(trees[0])):
            visible[x].append(check_visible(x,y,trees))
        logging.info(f'visibility :{visible[x]}')
        visible_sum+=sum(visible[x])


    return visible_sum

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

