import logging
import re

def print_map(sensors , no_beacons_map, beacons_map, x_range=range(-20, 25+1), y_range=range(-5,36+1)):
    sensors_map = set([ sensor for (sensor, beacon) in sensors])
    for y in y_range:
        line=f'{y:2}'
        for x in x_range:
            point = (x,y)
            if point in sensors_map:
                line += 'S'
            elif point in beacons_map:
                line += 'B'
            elif point in no_beacons_map:
                line += '#'
            else:
                line += '.'
        logging.info(f'map: {line}')

def read_input(stream):
    sensors = []
    for line in stream.readlines():
        sensor_x, sensor_y, beacon_x, beakon_y= map(int, re.findall(r"Sensor at x=(\d+), y=(\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)[0])
        sensors.append( ( (sensor_x, sensor_y), (beacon_x, beakon_y)))

    return sensors

def run(stream, row:int):
    sensors = read_input(stream)
    no_beacons_map = set()
    beacons_map = set()
    for sensor in sensors:
        (sensor_x, sensor_y), (beacon_x, beakon_y) = sensor
        beacons_map.add((beacon_x, beakon_y))
        distance = abs(beacon_x-sensor_x) + abs(beakon_y-sensor_y)
        logging.error(f'applying {sensor}, distance={distance}')
        width=0
        logging.info(f'startting x={range(sensor_x-distance, sensor_x+1)}')
        for x in range(sensor_x-distance, sensor_x+1):
            logging.info(f'startting y={range(sensor_y-width, sensor_y+width+1)}')
            for y in range(sensor_y-width, sensor_y+width+1):
                no_beacons_map.add((x,y))
            width+= 1
            #print_map(sensors , no_beacons_map, beacons_map)
        logging.info(f'startting x={range(sensor_x, sensor_x+distance+1)}')
        width-= 1
        for x in range(sensor_x, sensor_x+distance+1):
            logging.info(f'startting y={range(sensor_y-width, sensor_y+width+1)}')
            for y in range(sensor_y-width, sensor_y+width+1):
                no_beacons_map.add( (x,y))
            width-= 1
            #print_map(sensors , no_beacons_map, beacons_map)
        #break

    return  \
        len([position for position in list(no_beacons_map) if position[1] == row]) - \
        len([position for position in list(beacons_map) if position[1] == row])

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata, row=2000000))

