CUBES_LIMITS = {
    'red': 12,
    "green": 13,
    "blue": 14
}


def parse_input(input_str: str):
    games = []
    for game_line in input_str.split('\n'):
        game_line = game_line.strip()
        if not game_line:
            continue
        _game_id, cubes = game_line.split(':')
        game = []
        cubes = cubes.replace(';', ',')
        for single_cube_def in cubes.split(','):
            single_cube_def = single_cube_def.strip()
            count, cube_name = single_cube_def.split(' ')
            game.append((cube_name, int(count)))
        games.append(game)
    return games


def match_the_limits(cubes: list):
    for name, count in cubes:
        if count > CUBES_LIMITS[name]:
            return False
    return True


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)

    sum_of_game_ids = 0

    for game_id, cubes in enumerate(data, start=1):
        if match_the_limits(cubes):
            sum_of_game_ids += game_id
    return sum_of_game_ids


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
