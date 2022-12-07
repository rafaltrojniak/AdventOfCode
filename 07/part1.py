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

DIR_THRESHOLD = 100000

def find_tree_sizes(tree)-> tuple[int, int]:
    localsum=0 # Sum of files in current direcory and up
    totalsum=0 # Sum of directories where size is less than threshold

    for dirname, value in tree.items():
        if type(value) == dict:
            logging.info(f'calculating size for {dirname}')
            child_localsum, child_totalsum=find_tree_sizes(value)
            totalsum += child_totalsum
            logging.info(f'{dirname} resulted with {child_localsum}')
            localsum += child_localsum
            if child_localsum < DIR_THRESHOLD:
                logging.info(f'{dirname} added to totalsum {child_localsum}')
                totalsum += child_localsum
        else:
            localsum+=value

    return localsum, totalsum

def run(stream):
    tree = read_tree(stream)
    _, totalsum = find_tree_sizes(tree)
    return totalsum

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

