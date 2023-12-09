import sys
import re

if len(sys.argv) != 2:
    raise ValueError('Please provide path to the data.')

print(f'Path is {sys.argv[1]}')
path = sys.argv[1]

with open(path, 'r', encoding="utf-8") as f:
    lines = f.read().splitlines()

travel_time, distance = int(''.join(re.findall(r'\d+', lines[0]))), int(''.join(re.findall(r'\d+', lines[1])))
ways_to_win, hold_time = 0, 0
first_solution_found, no_solution = False, False

while True:
  hold_time += 1
  travel_time -=1

  if first_solution_found and no_solution:
    break

  if (hold_time * travel_time) > distance:
    ways_to_win += 1
    first_solution_found, no_solution = True, False
  else:
    no_solution = True

print(ways_to_win)