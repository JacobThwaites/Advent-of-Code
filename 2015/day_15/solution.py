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

ingredients = dd(dd)

for i, scores in input:
    for score in scores:
        name, val = score.split(' ')
        ingredients[i][name] = int(val)

def make_cookie(ingredient_ratios):
    cookie = {
        'capacity': 0,
        'durability': 0,
        'flavor': 0,
        'texture': 0,
        'calories': 0
    }
    score = 1
    
    for ingredient, ratio in ingredient_ratios:
        for property, value in ingredients[ingredient].items():
            cookie[property] += (ratio * value)
    
    # for k, v in cookie.items():
    #     if v < 0:
    #         cookie[k] = 0
            
    for key, value in cookie.items():
        if key != "calories":
            score *= value
    
    return score

remaining = 100

cookies = []

remaining = 100
max_score = 0

count = 0

for a in range(remaining + 1):
    for b in range(remaining - a + 1):
        for c in range(remaining - a - b + 1):
            d = remaining - a - b - c
            score = make_cookie([
                ('Sugar', a),
                ('Sprinkles', b),
                ('Candy', c),
                ('Cinnamon', d)
            ])
            max_score = max(max_score, score)

print(max_score)

# 129133440 - too high
# print(make_cookie([('Butterscotch', 44), ('Cinnamon', 56)]))


# 15862900 - too high
# 117936 - too low
