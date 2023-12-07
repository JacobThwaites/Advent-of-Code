import sys
import math
import bisect
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br

sys.setrecursionlimit(100000000)

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

mod=1000000007


def get_input():
    filename = './input.txt'
    # filename ='./test.txt'
    with open(filename, 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            line = line.split(' ')
            input.append(line)

        return input 

input = get_input()

# def secondary(hand):
#     scores = {
#         'A': 'm',
#         'K': 'l',
#         'Q': 'k',
#         'J': 'j',
#         'T': 'i',
#         '9': 'h',
#         '8': 'g',
#         '7': 'f',
#         '6': 'e',
#         '5': 'd',
#         '4': 'c',
#         '3': 'b',
#         '2': 'a',
#     }

#     s = ''

#     for card in hand:
#         s += scores[card]
    
#     return s


# def card_counts(str):
#     counts = dd(int)
#     for s in str:
#         counts[s] += 1
    
#     return counts

# def get_primary_score(counts):
#     scores = {
#         5: [],
#         4: [],
#         3: [],
#         2: [],
#         1: []
#     }

#     for k, count in counts.items():
#         scores[count].append(k)
    
#     if len(scores[5]) > 0:
#         return 7
    
#     if len(scores[4]) > 0:
#         return 6
    
#     if len(scores[3]) > 0:
#         if len(scores[2]) > 0:
#             return 5
#         else:
#             return 4
    
#     if len(scores[2]) == 2:
#         return 3

#     if len(scores[2]) == 1:
#         return 2

#     return 1

# hand_scores = []

# for hand in input:
#     counts = card_counts(hand[0])
#     primary_score = get_primary_score(counts)
#     h = {'hand': hand[0], 'bid': hand[1],'score': primary_score, 'secondary': secondary(hand[0])}
#     hand_scores.append(h)

# def get_sort_keys(obj):
#     return (obj['score'], obj['secondary'])

# sorted_hands = sorted(hand_scores, key=get_sort_keys)

# winnings = 0

# for i, s in enumerate(sorted_hands):
#     w = (i+1) * int(s['bid'])
#     winnings += w

# print(winnings)



# Part 2

def secondary(hand):
    scores = {
        'A': 'm',
        'K': 'l',
        'Q': 'k',
        'T': 'j',
        '9': 'i',
        '8': 'h',
        '7': 'g',
        '6': 'f',
        '5': 'e',
        '4': 'd',
        '3': 'c',
        '2': 'b',
        'J': 'a',
    }

    s = ''

    for card in hand:
        s += scores[card]

    return s


def card_counts(str):
    counts = dd(int)
    for s in str:
        counts[s] += 1
    
    return counts

def get_highest_count(scores):
    for n in range(5, 1, -1):
        if len(scores[n]) > 0:
            return n 
    
    return 1

def get_primary_score(counts):
    scores = {
        5: [],
        4: [],
        3: [],
        2: [],
        1: [],
        'J': 0
    }

    for k, count in counts.items():
        if k == 'J':
            scores['J'] += count
        else :
            scores[count].append(k)
    
    if scores['J'] > 0:
        highest_count = get_highest_count(scores)
        new_highest = highest_count + scores['J']
        if len(scores[highest_count]) > 1:
            first = scores[highest_count].pop()
            scores[new_highest] = [first]
        else:
            scores[new_highest] = scores[highest_count]
            scores[highest_count] = []
    
    if len(scores[5]) > 0:
        return 7
    
    if len(scores[4]) > 0:
        return 6
    
    if len(scores[3]) > 0:
        if len(scores[2]) > 0:
            return 5
        else:
            return 4
    
    if len(scores[2]) == 2:
        return 3

    if len(scores[2]) == 1:
        return 2

    return 1

hand_scores = []

for hand in input:
    counts = card_counts(hand[0])
    primary_score = get_primary_score(counts)
    h = {'hand': hand[0], 'bid': int(hand[1]),'score': primary_score, 'secondary': secondary(hand[0])}
    hand_scores.append(h)

def get_sort_keys(obj):
    return (obj['score'], obj['secondary'])

sorted_hands = sorted(hand_scores, key=get_sort_keys)

winnings = 0

for i, s in enumerate(sorted_hands):
    w = (i+1) * s['bid']
    winnings += w

print(winnings)
# 253926070
# 253630098