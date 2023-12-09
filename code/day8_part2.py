import sys
import re
import math

# Each --A node only reaches one --Z node in it's loop
# They all reach their --Z at the same "step" in the directions every time, meaning the loops are all a consistent period instead of changing or branching
# Conveniently the period it takes to reach the first --Z from the starting --A node is the same period as it takes to re-reach the --Z node when you're already there
# Above explanation taken from someone else, in short, every path is a perfect cycle with one "correct" end/beginning.

if len(sys.argv) != 2:
    raise ValueError('Please provide path to the data.')

print(f'Path is {sys.argv[1]}')
path = sys.argv[1]

with open(path, 'r', encoding="utf-8") as f:
    lines = f.read().splitlines()

# 0 is left, 1 is right. Good since I'm doing tuples for the paths
move_instructions = [(lambda x: 0 if x == "L" else 1)(move) for move in lines[0]]
path_instructions = {}
starting_nodes = []

for i in range(2, len(lines)):
  split_input = re.findall(r'[a-zA-Z]+', lines[i])
  # The key is path, the value is a tuple with the left and right path
  path_instructions[split_input[0]] = (split_input[1], split_input[2])
  # Find all starting nodes
  if split_input[0][2] == "A":
    starting_nodes.append(split_input[0])

shortest_paths = []
length_move_instructions = len(move_instructions)

# Find shortest path for each starting node. One complete cycle (not verified here)
for node in starting_nodes:
  current_next_path = node
  found_path = False
  shortest_path, move_index  = 0, 0
  while not found_path:
    current_left_right = path_instructions[current_next_path]
    left_or_right = move_instructions[move_index]
    shortest_path += 1

    if(current_left_right[left_or_right][2] == "Z"):
      found_path = True
    else:
      move_index += 1 
      if move_index >= len(move_instructions):
        move_index = 0
      current_next_path = current_left_right[left_or_right]
  shortest_paths.append(shortest_path)

print(shortest_paths)
# From a guy on the internet if you needed to calculate LCM on an array of ints.
# I added abs, just in case. Not needed here, but if someone else finds it
# reduce(lambda x,y:abs(x*y)//math.gcd(abs(x),abs(y)), shortest_paths)
print(math.lcm(*shortest_paths))