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
    with open('./input.txt', 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            combo = line.split('|')
            winners = combo[0].split(": ")[1]
            winners = winners.split(' ')
            winners = [w for w in winners if w != '']
            card_numbers = combo[1].split(' ')
            card_numbers = [c for c in card_numbers if c != '']
            input.append((winners, card_numbers))

        return input 

input = get_input()

def get_card_score(card):
    winners = {}
    nums = card[1]

    for w in card[0]:
        winners[w] = True
    
    score = 0
    for n in nums:
        if n in winners:
            if not score:
                score = 1 
            else:
                score *= 2

    return score

total = 0

for card in input:
    score = get_card_score(card)
    total += score

# print(total)

# Part 2

def get_card_matches(card):
    winners = {}
    nums = card[1]

    for w in card[0]:
        winners[w] = True
    
    score = 0
    for n in nums:
        if n in winners:
            score += 1

    return score

scores = {}

def dp(i):
    if i in scores:
        return scores[i]

    if i >= len(input):
        return 0
    
    card = input[i]    
    matches = get_card_matches(card)

    score = 1

    for m in range(1, matches+1):
        score += dp(i+m)

    scores[i] = score

    return scores[i]

i = len(input) - 1
while i >= 0:
    dp(i)
    i-=1

total = sum(scores.values())

print(total)