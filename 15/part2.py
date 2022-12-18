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


def get_normalized_sensor_ranges_for_row(sensors, row):
    for sensor in sensors:
        (sensor_x, sensor_y), distance= sensor
        width = distance - abs(sensor_y - row)
        if width >=0:
            yield range(sensor_x-width, sensor_x+width+1)


def normalize_sensors(sensors):
    normalized_sensors = []
    for sensor in sensors:
        (sensor_x, sensor_y), (beacon_x, beakon_y) = sensor
        distance = abs(beacon_x-sensor_x) + abs(beakon_y-sensor_y)
        normalized_sensors.append(((sensor_x, sensor_y), distance))
    return normalized_sensors

def get_tunint_frequency(x,y):
    return x*4000000+y

def run(stream, x_range:range, y_range:range):
    sensors = read_input(stream)
    normalized_sensors = normalize_sensors(sensors)
    for y in y_range:
        if y % 10000 == 0:
            logging.error(f'scanning row {y}')
        x_ranges = list(get_normalized_sensor_ranges_for_row(normalized_sensors , y))
        #logging.error(f'x_ranges pre-sort {x_ranges}')
        x_ranges.sort(key=lambda x: x.start)
        #logging.error(f'x_ranges post-sort {x_ranges}')
        x = x_range.start
        for r in x_ranges:
            if  x in r:
                x=r.stop
        if x in x_range:
            return get_tunint_frequency(x,y)

if __name__ == "__main__":
    with open('input.txt') as indata:
        #print(run(indata, x_range=range(0, 4000000+1), y_range=range(0,4000000+1)))
        print(run(indata, x_range=range(0, 4000000+1), y_range=range(3000000,4000000+1)))

