import sys
import numpy as np

if len(sys.argv) != 2:
    raise ValueError('Please provide path to the data.')

print(f'Path is {sys.argv[1]}')
path = sys.argv[1]

with open(path, 'r', encoding="utf-8") as f:
    lines = f.read().splitlines()

np_star_map = np.zeros((len(lines[0]), len(lines)))

for i, line in enumerate(lines):
    for j in range(len(lines[0])):
        np_star_map[i][j] = lines[i][j] == "#" if 1 else 0

empty_rows = reversed(list(np.where(~np_star_map.any(axis=1))[0]))
empty_columns = reversed(list(np.where(~np_star_map.any(axis=0))[0]))

for row in empty_rows:
    np_star_map = np.insert(np_star_map, row, values=0, axis=0)
for col in empty_columns:
    np_star_map = np.insert(np_star_map, col, values=0, axis=1)

galaxies_coord = np.transpose(np.nonzero(np_star_map)).tolist()
total_distance_combined = 0

for i, galaxy in enumerate(galaxies_coord):
    x_first, y_first = galaxy[1], galaxy[0]
    for j in range(i + 1, len(galaxies_coord)):
        second_cords = galaxies_coord[j]
        x_second, y_second = second_cords[1], second_cords[0]
        total_distance_combined += abs(x_first - x_second) + abs(y_first - y_second)

print(total_distance_combined)