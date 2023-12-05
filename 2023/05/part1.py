def parse_input(input_str: str):
    data = {

    }
    input_lines = input_str.strip().splitlines(keepends=False)
    seeds_line = input_lines.pop(0)
    data['seeds'] = list(map(int, seeds_line.split(':')[1].strip().split(' ')))
    input_lines.pop(0)  # One line after seeds

    maps = []
    current_map = []
    for map_line in input_lines:
        if not map_line:
            maps.append(current_map)
            current_map = []
            continue
        if map_line.endswith('map:'):
            continue
        current_map.append(
            list(map(int, map_line.split(' ')))
        )
    if current_map:
        maps.append(current_map)
    data['maps'] = maps

    return data


def map_locations(source_locations: int, maps: list[list]) -> int:
    for dest_start, src_start, range_len in maps:
        src_range = range(src_start, src_start + range_len)
        if source_locations in src_range:
            return source_locations - src_start + dest_start
    return source_locations


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    locations = []
    for location in data['seeds']:
        for mapping in data['maps']:
            location = map_locations(location, mapping)
        locations.append(location)
    return min(locations)

    pass


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
