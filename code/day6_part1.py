from functools import reduce
import sys
import re

if len(sys.argv) != 2:
    raise ValueError('Please provide path to the data.')

print(f'Path is {sys.argv[1]}')
path = sys.argv[1]

with open(path, 'r', encoding="utf-8") as f:
    lines = f.read().splitlines()

times, distances = re.findall(r'\d+', lines[0]), re.findall(r'\d+', lines[1])
ways_to_win = []

for i in range(len(times)):
    travel_time, distance = int(times[i]), int(distances[i])
    way_to_win, hold_time = 0, 0
    first_solution_found, no_solution = False, False

    while True:
      hold_time += 1
      travel_time -=1

      if first_solution_found and no_solution:
         break

      if (hold_time * travel_time) > distance :
        way_to_win += 1
        first_solution_found, no_solution = True, False
      else:
         no_solution = True

    ways_to_win.append(way_to_win)

print(reduce((lambda x, y: x * y), ways_to_win))