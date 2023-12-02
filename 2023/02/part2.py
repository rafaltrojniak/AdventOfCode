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


def get_minimal_cubes(game: list) -> dict:
    minimal = {}
    for cube, count in game:
        if cube in minimal:
            if minimal[cube] < count:
                minimal[cube] = count
        else:
            minimal[cube] = count

    return minimal


def calc_power(cubes: dict) -> int:
    power = 1
    for count in cubes.values():
        power *= count
    return power


def puzzle(input_str: str) -> int:
    data = parse_input(input_str)

    minimals = [get_minimal_cubes(game) for game in data]
    powers = [calc_power(minimal) for minimal in minimals]
    return sum(powers)


if __name__ == "__main__":
    with open('input.txt', 'r') as indata:
        print(puzzle(indata.read()))
