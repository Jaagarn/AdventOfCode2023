import sys
import numpy as np

if len(sys.argv) < 2:
    raise ValueError('Please provide path to the data.')

if len(sys.argv) < 3:
    raise ValueError('Please expansion variable.')

print(f'Path is {sys.argv[1]}')
print(f'Expansion variable is {sys.argv[2]}')

path = sys.argv[1]

# -1 to not include itself
expansion_var = int(sys.argv[2]) - 1

with open(path, 'r', encoding="utf-8") as f:
    lines = f.read().splitlines()

np_star_map = np.zeros((len(lines[0]), len(lines)))

for i, line in enumerate(lines):
    for j in range(len(lines[0])):
        np_star_map[i][j] = lines[i][j] == "#" if 1 else 0

empty_rows = np.where(~np_star_map.any(axis=1))[0].tolist()
empty_columns = np.where(~np_star_map.any(axis=0))[0].tolist()
galaxies_coord = np.transpose(np.nonzero(np_star_map)).tolist()

for i in range(len(galaxies_coord)):
    row, column = galaxies_coord[i][0], galaxies_coord[i][1]
    extra_rows, extra_columns = 0, 0
    for empty_row in empty_rows:
        if empty_row > row:
            break
        else:
            extra_rows += expansion_var
    for empty_column in empty_columns:
        if empty_column > column:
            break
        else:
            extra_columns += expansion_var
    galaxies_coord[i] = [row + extra_rows, column + extra_columns]

total_distance_combined = 0

for i, galaxy in enumerate(galaxies_coord):
    x_first, y_first = galaxy[1], galaxy[0]
    for j in range(i + 1, len(galaxies_coord)):
        distance_to = galaxies_coord[j]
        x_second, y_second = distance_to[1], distance_to[0]
        total_distance_combined += (abs(x_first - x_second) + abs(y_first - y_second))

print(total_distance_combined)