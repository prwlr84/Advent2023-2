from input import input
from math import prod


def split_games(string):
    string = string.replace('Game ', '')
    game_id, play = string.split(': ')
    play = list(map(lambda s: list(map(lambda x: tuple(x.split()), s.split(', '))), play.split('; ')))
    return [game_id, play]


def get_games(string):
    games = {}
    strings = string.split('\n')
    for game in strings:
        k, v = split_games(game)
        games[k] = v

    return games


def get_sum_of_ids(string):
    sets = {'blue': 14, 'green': 13, 'red': 12}
    ids = []
    games = get_games(string)

    for k, v in games.items():
        for g in v:
            for t in g:
                if int(t[0]) > sets[t[1]]:
                    ids.append(int(k))

    print(sum(set(range(100)) - set(ids)))


def get_cube_powers(string):
    games = get_games(string)
    powers_list = []
    for v in games.values():
        colors = {'red': [], 'blue': [], 'green': []}
        flat_list = [item for sublist in v for item in sublist]
        for i in flat_list:
            colors[i[1]].append(int(i[0]))
        powers_list.append(prod([max(k) for k in colors.values()]))

    print(sum(powers_list))


if __name__ == '__main__':
    get_sum_of_ids(input)
    get_cube_powers(input)
