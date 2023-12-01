import copy
import sys
import re

def str_to_number(input_str):
    inside_str = copy.copy(input_str)
    if(inside_str.isdigit()):
        return inside_str
    
    match inside_str:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"

def add_extra_letters(input_str):
    #This is to read twone as 21(twoone) as an example. Might be overkill
    inside_str = copy.copy(input_str)

    match inside_str:
        case "one":
            return "oonee"
        case "two":
            return "ttwoo"
        case "three":
            return "tthree"
        case "five":
            return "fivee"
        case "seven":
            return "sevenn"
        case "eight":
            return "eeightt"
        case "nine":
            return "nninee"
    return inside_str
         
def find_numbers(input_str):
    #Split on numbers with potential issues, i.e twone should be 21 and not 22
    #Add extra letters to avoid above issue
    #Join the result as a "safe" string without the issues.
    #Return the list of numbers as text and ints

    inside_str = copy.copy(input_str)
    
    unsafe_str_list = re.split(r'(one|two|three|five|eight|seven|nine)', inside_str)

    safe_string = ''.join([add_extra_letters(unsafe_str) for unsafe_str in unsafe_str_list])

    return re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', safe_string)

if len(sys.argv) != 2:
    raise ValueError('Please provide path to the data.')

print(f'Path is {sys.argv[1]}')

path = sys.argv[1]

with open(path, 'r', encoding="utf-8") as f:
    lines = f.readlines()

#Remove all irrelevant chars
only_digits = [find_numbers(line) for line in lines]

#Add the first and last number togheter and then turn it to an int. str 1 + 2 = 12, and int 1 + 2 = 3
result = [int(str_to_number(digits[0]) + str_to_number(digits[-1])) for digits in only_digits]

print(sum(result))
