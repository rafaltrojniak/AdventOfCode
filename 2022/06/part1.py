import logging


def run(data):
    n=4
    data=list(data)
    while not len(set( data[0:4]))==4:
        del data[0]
        n+=1
    logging.info('found marker at '+str(data[0:4]))
    return n

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata.read()))

