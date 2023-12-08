# WARNING: This is extremly un-optimized and may take several (!) hours to run.
# I will refactor at some point to checking ranges (1, 3) => (1, 2) (4) instead of individual seeds [ 1, 2, 3 ] => [ 1, 2, 4 ]

import sys
import re

def extract_paths(input_lines, start_index):
    dest_source_ranges = []
    for j in range(start_index, len(input_lines)):
        if(re.match(r'\d', lines[j]) != None):
            dest_source_ranges.append(list(filter(None, re.split(r' ', lines[j]))))
        else:
            return dest_source_ranges, j
    return dest_source_ranges, j

def reallocate_seed(seed, dest_source_ranges):
    for one_line in dest_source_ranges:
        dest, source, ranges = int(one_line[0]), int(one_line[1]), int(one_line[2])
        if(seed >= source and seed < source + ranges):
            return dest + (seed - source)
    return seed

if len(sys.argv) != 2:
    raise ValueError('Please provide path to the data.')

print(f'Path is {sys.argv[1]}')
path = sys.argv[1]

with open(path, 'r', encoding="utf-8") as f:
    lines = f.read().splitlines()

unfinished_seeds = list(filter(None, re.split(r'seeds:| ', lines[0])))
seeds = []
seed_index = 0

while seed_index < len(unfinished_seeds)-1:
    print(seed_index)
    first, second = int(unfinished_seeds[seed_index]), int(unfinished_seeds[seed_index+1])
    seeds.extend(range(first, first+second))
    seed_index += 2

print("All seeds processed")
all_dest_source_ranges = []
index = 3

while index < len(lines) - 1:
    result = extract_paths(lines, index)
    all_dest_source_ranges.append(result[0])
    index = result[1] + 2
print("All dest_source_ranges processed")

for dest_source_range in all_dest_source_ranges:
    for i in range(len(seeds)):
        seeds[i] = reallocate_seed(int(seeds[i]), dest_source_range)
    print("One dest_source_range_complete")

print(min(seed for seed in seeds))