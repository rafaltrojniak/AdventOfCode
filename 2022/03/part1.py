import logging

LOWER_BASE=ord('a')-1
UPPER_BASE=ord('A')-1
def priority(char):
    char_number = ord(char)
    if char_number > LOWER_BASE:
        return char_number-LOWER_BASE
    return char_number-UPPER_BASE + 26

def run(stream):
    priority_sum=0
    for line in stream.readlines():
        line.strip()
        size = len(line)
        [common]=set(line[0:int(size/2)]) & set(line[int(size/2):size])
        logging.info((line[0:int(size/2)],line[int(size/2):size]))
        logging.info(common)
        logging.info(priority(common))
        priority_sum+=priority(common)
    return priority_sum

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

