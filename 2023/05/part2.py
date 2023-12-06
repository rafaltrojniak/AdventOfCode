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


def check_ranges_intersect(r1: range, r2: range) -> bool:
    return bool(range(max(r1.start, r2.start), min(r1.stop, r2.stop)))


def map_ranges(source_location: range, src_range: range, dst_range: range) \
        -> tuple[list[range], list[range]]:
    unmapped_ranges = []
    if source_location.start < src_range.start:
        unmapped_ranges.append(
            range(source_location.start, src_range.start)
        )
    if source_location.stop > src_range.stop:
        unmapped_ranges.append(
            range(src_range.stop, source_location.stop)
        )
    progress = dst_range.start - src_range.start
    mapped_range = range(
        max(source_location.start, src_range.start) + progress,
        min(source_location.stop, src_range.stop) + progress
    )
    return mapped_range, unmapped_ranges


def map_locations(org_ranges: list[range], maps: list[range]) -> list[range]:
    processed_ranges = []
    for src_range, dst_range in maps:
        unprocessed_ranges = []
        while org_ranges:
            org_range = org_ranges.pop()
            if not check_ranges_intersect(src_range, org_range):
                unprocessed_ranges.append(org_range)
                continue
            mapped_range, not_mapped_ranges = map_ranges(org_range, src_range, dst_range)
            unprocessed_ranges += not_mapped_ranges
            processed_ranges.append(mapped_range)
        org_ranges = unprocessed_ranges
    return processed_ranges + org_ranges


def model_ranges(data: dict):
    data_in_ranges: {}
    seeds_copy = data['seeds'].copy()
    seed_ranges = []
    while seeds_copy:
        seed_range_start = seeds_copy.pop(0)
        seed_range_len = seeds_copy.pop(0)
        seed_range = range(seed_range_start,
                           seed_range_start + seed_range_len)
        seed_ranges.append(seed_range)

    maps_in_ranges = []
    for maps in data['maps']:
        map_in_ranges = []
        for dest_start, src_start, range_len in maps:
            map_in_ranges.append(
                (range(src_start, src_start + range_len),
                 range(dest_start, dest_start + range_len),
                 )
            )
        maps_in_ranges.append(map_in_ranges)

    data_in_ranges = {
        'seeds': seed_ranges,
        'maps': maps_in_ranges
    }
    return data_in_ranges


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)
    data_in_ranges = model_ranges(data)
    locations = data_in_ranges['seeds']
    for mapping in data_in_ranges['maps']:
        locations = map_locations(locations, mapping)
    return min([range.start for range in locations])


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
