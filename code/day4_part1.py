import sys
import re

def points_per_card(input_str):
    split_input = re.split(r':|\|', input_str)
    split_play_nrs = re.split(" ", split_input[1])
    split_win_nrs = re.split(" ", split_input[2])

    matches = len(set(split_play_nrs).intersection(split_win_nrs)) - 1
    
    return matches == 0 if 0 else int(pow(2, matches-1))

if len(sys.argv) != 2:
    raise ValueError('Please provide path to the data.')

print(f'Path is {sys.argv[1]}')
path = sys.argv[1]

with open(path, 'r', encoding="utf-8") as f:
    lines = f.read().splitlines()

total_value = 0

for line in lines:
    total_value += points_per_card(line)

print(total_value)