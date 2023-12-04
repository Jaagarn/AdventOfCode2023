import sys
import re

def matches(input_sym, input_match_nr_list):
    matching_nr = []
    for match_nr in input_match_nr_list:
        for nr in match_nr:
            first_nr = nr.span()[0] - 1
            #Python is inclusive, otherwise +1 here
            second_nr = nr.span()[1]
            sym_pointer = input_sym.span()[0]
            if sym_pointer >= first_nr and sym_pointer <= second_nr:
                matching_nr.append(nr.group(0))
    if(len(matching_nr) == 2):
        return int(matching_nr[0])*int(matching_nr[1])
    return 0                 

if len(sys.argv) != 2:
    raise ValueError('Please provide path to the data.')

print(f'Path is {sys.argv[1]}')

path = sys.argv[1]

with open(path, 'r', encoding="utf-8") as f:
    lines = f.read().splitlines()

matches_numbers = [list(re.finditer(r'\d+', line)) for line in lines]
matches_symbols = [list(re.finditer(r'[\*]', line)) for line in lines]

total_value = 0

for i in range(len(lines)):
    match_sym = matches_symbols[i]
    match_nrs_list = []
    match_nrs_list.append(matches_numbers[i])
    if i != 0:
        match_nrs_list.append(matches_numbers[i-1])
    if i != len(lines) - 1:
        match_nrs_list.append(matches_numbers[i+1])
    
    for sym in match_sym:
        match_value = matches(sym, match_nrs_list)
        total_value += match_value

print(total_value)