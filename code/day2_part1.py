import sys
import re

#Red, Green, Blue
MAX_CUBES = [12, 13, 14]

def valid_game(input_game):
    round_split = input_game.split(";")

    for cube_round in round_split:
        seperated_cubes = cube_round.split(",")
        for cube in seperated_cubes:
            cube = cube.split()
            number = int(cube[0])
            match cube[1]:
                case "red":
                    if number > MAX_CUBES[0]:
                        return False
                case "green":
                    if number > MAX_CUBES[1]:
                        return False
                case "blue":
                    if number > MAX_CUBES[2]:
                        return False
    return True

def game_ids_added(game_input):
    total_value = 0
    for game in game_input:
        split_game = game.split(":")
        if(valid_game(split_game[1])):
            extract_id = split_game[0].split()
            total_value = total_value + int (extract_id[1])
    return total_value

if len(sys.argv) != 2:
    raise ValueError('Please provide path to the data.')

print(f'Path is {sys.argv[1]}')

path = sys.argv[1]

with open(path, 'r', encoding="utf-8") as f:
    lines = f.read().splitlines()

print(game_ids_added(lines))
