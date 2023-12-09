import sys
import re

if len(sys.argv) != 2:
    raise ValueError('Please provide path to the data.')

print(f'Path is {sys.argv[1]}')
path = sys.argv[1]

with open(path, 'r', encoding="utf-8") as f:
  lines = f.read().splitlines()

move_instructions = [(lambda x: 0 if x == "L" else 1)(move) for move in lines[0]]
path_instructions = {}

for i in range(2, len(lines)):
  split_input = re.findall(r'[a-zA-Z]+', lines[i])
  path_instructions[split_input[0]] = (split_input[1], split_input[2])

found_path = False
shortest_path, move_index, length_move_instructions = 0, 0, len(move_instructions)
current_next_path = "AAA"

while not found_path:
  current_left_right = path_instructions[current_next_path]
  left_or_right = move_instructions[move_index]
  shortest_path += 1

  if(current_left_right[left_or_right] == "ZZZ"):
    found_path = True
  else:
    move_index += 1 
    if move_index >= len(move_instructions):
      move_index = 0
    current_next_path = current_left_right[left_or_right]

print(shortest_path)