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

def log_stripe(index):
    stripe=['.']*40
    stripe[index-1:index+1]='###'
    stripe = ''.join(stripe)
    logging.info(f'stripe: {stripe}')
def log_beam(index):
    stripe=['.']*40
    stripe[index]='@'
    stripe = ''.join(stripe)
    logging.info(f'beam  : {stripe}')

def get_pixel(signal, position):
    if signal in [position-1, position, position+1]:
        return '#'
    return '.'

def run(stream):
    signal = parse_signal(stream)
    width = 40
    output=''
    for line in range(0,len(signal),width):
        for index in range(0,width):
            signal_now = signal[line+index]
            log_stripe(signal_now)
            log_beam(index)
            output+=get_pixel(signal_now, index)
        output += '\n'
    return output

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

