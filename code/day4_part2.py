import sys
import re

def points_per_card(input_str):
    split_input = re.split(r':|\|', input_str)
    split_play_nrs = re.split(" ", split_input[1])
    split_win_nrs = re.split(" ", split_input[2])

    matches = len(set(split_play_nrs).intersection(split_win_nrs)) - 1
    
    return matches
     
if len(sys.argv) != 2:
    raise ValueError('Please provide path to the data.')

print(f'Path is {sys.argv[1]}')
path = sys.argv[1]

with open(path, 'r', encoding="utf-8") as f:
    lines = f.read().splitlines()

tracker = {key: 1 for key in range(len(lines))}

for i in range(len(lines)):
    winnings = points_per_card(lines[i])
    add_amount = tracker[i]
    for j in range(i + 1, winnings + i + 1):
        tracker[j] = tracker[j] + add_amount

print(sum(tracker.values()))
