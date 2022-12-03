from re import M
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
            com = line.split(' ')
            input.append(com)

        return input 

input = get_input()
# print(input)

draws = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

loses = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

wins = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

points = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

t = 0

# Part 1
# for x in input:
#     if loses[x[0]] == x[1]:
#         t += points[x[1]]
#     elif draws[x[0]] == x[1]:
#         t += (3 + points[x[1]])
#     else: 
#         t += (6 + points[x[1]])


# Part 2
for x in input:
    if x[1] == 'X':
        t += points[loses[x[0]]]
    elif x[1] == 'Y':
        t += 3 + points[draws[x[0]]]
    else:
        t += 6 + points[wins[x[0]]]

print(t)