import sys
import re

if len(sys.argv) != 2:
    raise ValueError('Please provide path to the data.')

print(f'Path is {sys.argv[1]}')

path = sys.argv[1]

with open(path, 'r', encoding="utf-8") as f:
    lines = f.readlines()

only_digits = [re.findall(r'\d', line) for line in lines]

result = [int(digits[0] + digits[-1]) for digits in only_digits]

print(sum(result))
