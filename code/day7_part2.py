import sys
import copy
from collections import Counter
from functools import cmp_to_key

CARDS = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
CARDS_VALUE = list(range(len(CARDS)))
CARDS_VALUE_DIC = dict(zip(CARDS, CARDS_VALUE))

#Type 0-6, 0 being the worst and 6 being the best
def return_hand_type(input_hand):
    copy_hand = copy.copy(input_hand)
    unique_and_amount = dict(Counter(copy_hand))

    if "J" in unique_and_amount.keys():
      how_many_j = unique_and_amount["J"]
      if how_many_j >= 4:
        return 6
      unique_and_amount = dict(sorted(unique_and_amount.items(), key=lambda x:x[1], reverse=True))
      most_cards = list(unique_and_amount.keys())[0]
      if(most_cards == "J"):
        most_cards = list(unique_and_amount.keys())[1]
      unique_and_amount[most_cards] += how_many_j
      unique_and_amount.pop("J", None)
    
    match len(unique_and_amount.keys()):
        case 1:
            return 6
        case 2:
            most_of_unique = sorted(list(unique_and_amount.values()), reverse=True)[0]
            if most_of_unique == 4 :
                return 5 
            else: 
                return 4 
        case 3:
            most_of_unique = sorted(list(unique_and_amount.values()), reverse=True)[0]
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
    all_hands_unsorted.append([split_line[0], return_hand_type(split_line[0]), int(split_line[1])])

all_hands_sorted = sorted(all_hands_unsorted, key=cmp_to_key(return_highest_hand))
total_winnings = 0

for i in range(len(all_hands_sorted)):
    total_winnings += (all_hands_sorted[i][2] * (i+1))

print(total_winnings)