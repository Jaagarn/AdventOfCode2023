import sys
import re

def matches(input_nr, input_match_sym_list):
    for match_sym in input_match_sym_list:
        for sym in match_sym:
            first_nr = input_nr.span()[0] - 1
            #Python is inclusive, otherwise +1 here
            second_nr = input_nr.span()[1]
            sym_pointer = sym.span()[0]
            if sym_pointer >= first_nr and sym_pointer <= second_nr:
                return int(input_nr.group(0))
    return 0
                        

if len(sys.argv) != 2:
    raise ValueError('Please provide path to the data.')

print(f'Path is {sys.argv[1]}')

path = sys.argv[1]

with open(path, 'r', encoding="utf-8") as f:
    lines = f.read().splitlines()

matches_numbers = [list(re.finditer(r'\d+', line)) for line in lines]

matches_symbols = [list(re.finditer(r'[^\d\.]', line)) for line in lines]

total_value = 0

for i in range(len(lines)):
    if i == 0:
        match_nrs = matches_numbers[i]
        match_sym_list = []
        match_sym_list.append(matches_symbols[i])
        match_sym_list.append(matches_symbols[i+1])
        for nr in match_nrs:
            match_value = matches(nr, match_sym_list)
            total_value = match_value + total_value
    elif i == len(lines) - 1:
        match_nrs = matches_numbers[i]
        match_sym_list = []
        match_sym_list.append(matches_symbols[i-1])
        match_sym_list.append(matches_symbols[i])
        for nr in match_nrs:
            match_value = matches(nr, match_sym_list)
            total_value = match_value + total_value
    else:
        match_nrs = matches_numbers[i]
        match_sym_list = []
        match_sym_list.append(matches_symbols[i-1])
        match_sym_list.append(matches_symbols[i])
        match_sym_list.append(matches_symbols[i+1])
        for nr in match_nrs:
            match_value = matches(nr, match_sym_list)
            total_value = match_value + total_value

print(total_value)