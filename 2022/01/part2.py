import sys

summaries = []
current = 0

def separator():
    global summaries
    global current
    summaries.append(current)
    current=0


for line in sys.stdin.readlines():
    if line == '\n':
        separator()
        continue
    current += int(line)
separator()

summaries.sort(reverse=True)
print(sum(summaries[0:3]))
