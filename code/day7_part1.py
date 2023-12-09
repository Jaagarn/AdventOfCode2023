import sys
import copy
from collections import Counter
from functools import cmp_to_key

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
CARDS_VALUE = list(range(len(CARDS)))
CARDS_VALUE_DIC = dict(zip(CARDS, CARDS_VALUE))

#Type 0-6, 0 being the worst and 6 being the best
def hand_type(input_hand):
    copy_hand = copy.copy(input_hand)
    unique = list(set(copy_hand))

    match len(unique):
        case 1:
            return 6
        case 2:
            most_of_unique = sorted(list(Counter(copy_hand).values()), reverse=True)[0]
            if most_of_unique == 4:
                return 5
            else: 
                return 4
        case 3:
            most_of_unique = sorted(list(Counter(copy_hand).values()), reverse=True)[0]
            if most_of_unique == 3:
                return 3
            else: 
                return 2
        case 4:
            return 1
        case 5:
            return 0

def return_highest_hand(hand1, hand2):
    if hand1[1] == hand2[1]:
        for i in range(5):
            hand1_card = CARDS_VALUE_DIC[hand1[0][i]]
            hand2_card = CARDS_VALUE_DIC[hand2[0][i]]
            if hand1_card > hand2_card:
                return 1
            if hand1_card < hand2_card:
                return -1
        return 0
    if hand1[1] > hand2 [1]:
        return 1
    if hand1[1] < hand2 [1]:
        return -1
    #Unnecessary default
    return 0
    

print(f'Path is {sys.argv[1]}')
path = sys.argv[1]

with open(path, 'r', encoding="utf-8") as f:
    lines = f.read().splitlines()

all_hands_unsorted = []

for line in lines:
    split_line = line.split()
    all_hands_unsorted.append([split_line[0], hand_type(split_line[0]), int(split_line[1])])

all_hands_sorted = sorted(all_hands_unsorted, key=cmp_to_key(return_highest_hand))
total_winnings = 0

for i in range(len(all_hands_sorted)):
    total_winnings += (all_hands_sorted[i][2] * (i+1))

print(total_winnings)