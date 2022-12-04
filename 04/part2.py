import logging

def check_overlap(line):
    [ range1, range2] = line.split(',')
    range1=[int(x) for x in range1.split('-')]
    range2=[int(x) for x in range2.split('-')]
    if range2[1]<range1[0] or range1[1] < range2[0]:
        return False
    return True
#    if (range1[0]<=range2[0] and range1[1]>=range2[1]) or \ # range1 in range2
#      (range2[0]<=range1[0] and range2[1]>=range1[1]) or \ # range2 in range1
#      return True

#    return False

def run(stream):
    return sum(
        [ check_overlap(line.strip()) for line in stream.readlines()]
        )

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

