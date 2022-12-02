import sys

maximal = 0
current = 0

def separator():
    global current
    global maximal
    if current > maximal:
        maximal=current
    current=0


for line in sys.stdin.readlines():
    if line == '\n':
        separator()
        continue
    current += int(line)
separator()
print(maximal)
