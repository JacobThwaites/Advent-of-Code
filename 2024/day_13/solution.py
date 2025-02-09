import sys
import math
import bisect
import re
from math import gcd,floor,sqrt,log, prod
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
        content = file.read()
        puzzles = content.strip().split('\n\n')
        input = []

        for p in puzzles:
            a, b, prize = p.split('\n')
            a = a.replace('X+', '')
            a = a.replace('Y+', '')
            a = a.replace(',', '')
            a = a.split(' ')
            a = [int(a[2]), int(a[3])]
            
            b = b.replace('X+', '')
            b = b.replace('Y+', '')
            b = b.replace(',', '')
            b = b.split(' ')
            b = [int(b[2]), int(b[3])]
            
            prize = prize.replace('X=', '')
            prize = prize.replace('Y=', '')
            prize = prize.replace(',', '')
            prize = prize.split(' ')
            prize = [int(prize[1]), int(prize[2])]
            input.append([a, b, prize])
        return input

input = get_input()
# [print(row) for row in input]

def find_min(a, b, target):
    mn = float('inf')
    a_target, b_target = target
    prizes_won = 0

    for x in range(100):
        a_calc = [(a[0] * x), a[1] * x]
        for y in range(100):
            b_calc = [b[0] * y, b[1] * y]
            if a_calc[0] + b_calc[0] == a_target:
                if a_calc[1] + b_calc[1] == b_target:
                    if (3*x)+y < mn or prizes_won < 2:
                        mn = (3*x)+y
                        prizes_won = 2
                elif prizes_won == 0:
                    mn = (3*x)+y
                    prizes_won = 1
            elif a_calc[1] + b_calc[1] == b_target and prizes_won == 0:
                mn = (3*x)+y
                prizes_won = 1
            elif a_calc[0] + b_calc[0] > a_target or a_calc[1] + b_calc[1] > b_target:
                break

    if mn == float('inf'):
        return 0
    return mn

total = 0
for a, b, target in input:
    total += find_min(a, b, target)
    
print(total)

# 46106 - too high
