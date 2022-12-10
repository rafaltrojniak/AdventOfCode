import logging

def parse_signal(stream):
    value = 1
    signal=[]
    for line in stream.readlines():
        signal.append(value)
        if line.startswith('addx'):
            _,operand = line.strip().split(' ')
            signal.append(value)
            value+= int(operand)
    return signal

def run(stream):
    signal = parse_signal(stream)
    position = 20
    step = 40
    signal_strength_sum=0
    while position <len(signal):
        signal_strength_sum+=position * signal[position-1]
        position += step
    return signal_strength_sum

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

