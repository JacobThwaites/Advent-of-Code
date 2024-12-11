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
        input = []
        for line in file: 
            line = line.replace('\n', '')
            return [int(x) for x in line.split(' ')]

        return input 

input = get_input()
# [print(row) for row in input]

def process(stone):
    if stone == 0:
        return [1]
    
    s = str(stone)
    if len(s) % 2 == 0:
        return [int(s[:len(s)//2]), int(s[len(s)//2:])]
    
    return [stone * 2024]

stone_counts = dd(int)

for stone in input:
    stone_counts[stone] += 1

conversions = {}

for _ in range(75):
    new_stone_counts = dd(int)
    for stone, count in stone_counts.items():
        if stone not in conversions:
            conversions[stone] = process(stone)
            
        for key in conversions[stone]:
            new_stone_counts[key] += count
    stone_counts = new_stone_counts

print(sum(stone_counts.values()))