import logging

def read_tree(stream):
    tree={}
    cwd=[tree]
    for line in stream.readlines():
        line=line.strip()
        if line.startswith('$ cd'):
            _,_,dirname = line.split(' ')
            logging.info(f'CD section with {dirname}')
            if dirname == '/':
                cwd = [tree]
            elif dirname == '..':
                cwd.pop()
            else:
                logging.info(f'adding dir {dirname}')
                newdir = {}
                cwd[-1][dirname]=newdir
                cwd.append(newdir)
        elif line.startswith('$ ls'):
            continue
        else:
            size, name = line.split(' ')
            if size == 'dir':
                continue
            cwd[-1][name]=int(size)
    return tree

TOTAL_SPACE = 70000000
NEEDED_SPACE = 30000000


def get_all_space(tree):
    used_size = 0
    for value in tree.values():
        if type(value) == dict:
            used_size += get_all_space(value)
        else:
            used_size += value
    return used_size

def find_tree_sizes(tree):
    localsum=0 # Sum of files in current direcory and up
    allsums=[]

    for dirname, value in tree.items():
        if type(value) == dict:
            logging.info(f'calculating size for {dirname}')
            child_localsum, child_allsums=find_tree_sizes(value)
            logging.info(f'{dirname} resulted with {child_localsum}')
            localsum += child_localsum
            allsums+=child_allsums
        else:
            localsum+=value

    allsums+=[localsum]
    return localsum, allsums

def run(stream):
    tree = read_tree(stream)
    used_size = get_all_space(tree)
    logging.info(f'Total used size is {used_size}')
    needed_size = NEEDED_SPACE - (TOTAL_SPACE-used_size)
    logging.info(f'we need {needed_size}')
    _, allsums= find_tree_sizes(tree)
    allsums.sort()
    return [value for value in allsums if value >= needed_size][0]

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

