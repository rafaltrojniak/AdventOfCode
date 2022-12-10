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

def run(stream):
    signal = parse_signal(stream)
    width = 40
    output=''
    for line in range(0,6):
        #logging.info(f'analysing line {line}')
        for index in range(0,width):
            logging.info(f'analysing position {index}')
            position = line*width+index
            if position >=len(signal):
                logging.error(f'Got out of the signal boundaries')
                return output
            signal_now = signal[position]
            logging.info(f'Signalis at {signal_now}')
            sprite_range = range(index-1,index+2)
            logging.info(f'Sprinte rane {sprite_range }')
            log_stripe(signal_now)
            log_beam(index)
            if signal_now in sprite_range :
                value = '#'
            else:
                value = '.'
            output += value
            logging.info(f'Result  {output}')
        output += '\n'
    return output

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata))

