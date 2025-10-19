import re
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
            name, scores = line.split(': ')
            scores = scores.split(', ')

            input.append((name, scores))

        return input

input = get_input()

ingredients = {}

for i, scores in input:
    ingredients[i] = {}
    for score in scores:
        name, val = score.split(' ')
        ingredients[i][name] = int(val)

def get_cookie_score(ingredient_ratios):
    # calories = 0
    # for (name, total)  in ingredient_ratios:
    #     ingredient_calories = ingredients[name]['calories']
    #     if total > 0:
    #         calories += total * ingredient_calories

    # if calories != 500:
    #     return float('inf')

    cookie = {
        'capacity': 0,
        'durability': 0,
        'flavor': 0,
        'texture': 0,
        'calories': 0
    }
    for ingredient, ratio in ingredient_ratios:
        for property, value in ingredients[ingredient].items():
            cookie[property] += (ratio * value)

    if cookie['calories'] != 500:
        return 0

    score = 1
    for key in ['capacity', 'durability', 'flavor', 'texture']:
        score *= max(0, cookie[key])

    return score


remaining = 100
max_score = 0

# Use actual ingredient names from input
names = [i for i, _ in input]
a_name, b_name, c_name, d_name = names

for a in range(remaining + 1):
    for b in range(remaining - a + 1):
        for c in range(remaining - a - b + 1):
            d = remaining - a - b - c
            score = get_cookie_score([
                (a_name, a),
                (b_name, b),
                (c_name, c),
                (d_name, d)
            ])
            max_score = max(max_score, score)

print(max_score)
