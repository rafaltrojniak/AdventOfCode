import logging

LOWER_BASE=ord('a')-1
UPPER_BASE=ord('A')-1
def priority(char):
    char_number = ord(char)
    if char_number > LOWER_BASE:
        return char_number-LOWER_BASE
    return char_number-UPPER_BASE + 26

def parse_stack(stack):
    logging.info(stack)
    sets=[set(list(x)) for x in stack]
    logging.info(sets)
    results = (sets[0]& sets[1] & sets[2])
    logging.info(results)
    return priority(results.pop())

def run(stream):
    priority_sum=0
    stack=[]
    for line in stream.readlines():
        stack.append(line.strip())
        if len(stack)>=3:
            priority_sum+=parse_stack(stack)
            stack=[]
    return priority_sum

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

