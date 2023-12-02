import sys
import re

def cal_minimum_cubes(input_game):
    minimum_cubes = [1, 1, 1]
    round_split = input_game.split(";")

    for cube_round in round_split:
        seperated_cubes = cube_round.split(",")
        for cube in seperated_cubes:
            cube = cube.split()
            number = int(cube[0])
            match cube[1]:
                case "red":
                    if number > minimum_cubes[0]:
                        minimum_cubes[0] = number
                case "green":
                    if number > minimum_cubes[1]:
                        minimum_cubes[1] = number
                case "blue":
                    if number > minimum_cubes[2]:
                        minimum_cubes[2] = number

    return minimum_cubes[0]*minimum_cubes[1]*minimum_cubes[2]

def iterate_games(game_input):
    total_value = 0

    for game in game_input:
        split_game = game.split(":")
        total_value = total_value+cal_minimum_cubes(split_game[1])

    return total_value

if len(sys.argv) != 2:
    raise ValueError('Please provide path to the data.')

print(f'Path is {sys.argv[1]}')

path = sys.argv[1]

with open(path, 'r', encoding="utf-8") as f:
    lines = f.read().splitlines()

print(iterate_games(lines))
