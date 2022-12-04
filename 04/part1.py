import logging

def check_full_overlap(line):
    [ range1, range2] = line.split(',')
    range1=tuple(map(int, range1.split('-')))
    range2=tuple(map(int, range2.split('-')))
    if (range1[0]<=range2[0] and range1[1]>=range2[1]) or \
      (range2[0]<=range1[0] and range2[1]>=range1[1]):
      return True

    return False

def run(stream):
    return sum(
        [ check_full_overlap(line.strip()) for line in stream.readlines()]
        )

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

