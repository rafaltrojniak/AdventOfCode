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

def get_sensor_range_for_row(sensor, row):
    (sensor_x, sensor_y), (beacon_x, beakon_y) = sensor
    distance = abs(beacon_x-sensor_x) + abs(beakon_y-sensor_y)
    #logging.error(f'applying {sensor}, distance={distance}')
    #logging.info(f'startting x={range(sensor_x-distance, sensor_x+1)}')
    width = distance - abs(sensor_y - row)
    if width >=0:
        return range(sensor_x-width, sensor_x+width+1)
    else:
        return range(0,0)

def get_tunint_frequency(x,y):
    return x*4000000+y

def run(stream, x_range:range, y_range:range):
    sensors = read_input(stream)
    for y in y_range:
        logging.error(f'scanning row {y}')
        x_ranges = [get_sensor_range_for_row(sensor, y) for sensor in sensors]
        x = 0
        while x in x_range:
            problematic_range = [ r for r in x_ranges if x in r]
    #        logging.info(f'found problematic range {problematic_range}')
            if not problematic_range :
                return get_tunint_frequency(x,y)
            x=max([r.stop for r in  problematic_range])

if __name__ == "__main__":
    with open('input.txt') as indata:
        print(run(indata, x_range=range(0, 4000000+1), y_range=range(0,4000000+1)))

