import logging

def check_overlap(line):
    [ range1, range2] = line.split(',')
    range1=tuple(map(int, range1.split('-')))
    range2=tuple(map(int, range2.split('-')))
    if range2[1]<range1[0] or range1[1] < range2[0]:
        return False
    return True

def run(stream):
    return sum(
        [ check_overlap(line.strip()) for line in stream.readlines()]
        )

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

