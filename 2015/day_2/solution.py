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

def max_index(arr):
    index = 0
    mx = float('-inf')

    for i, v in enumerate(arr):
        if v > mx:
            mx = v
            index = i
    
    return index

def min_index(arr):
    index = 0
    mn = float('inf')

    for i, v in enumerate(arr):
        if v < mn:
            mn = v
            index = i
    
    return index


def get_input():
    with open('./input.txt', 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            line = line.split('x')
            for i, c in enumerate(line):
                line[i] = int(c)
            input.append((line[0], line[1], line[2]))

        return input 

input = get_input()

total = 0 
for x in input:
    l,w,h = x
    total += 2 * l 
    total += 2 *  w 
    total += 2 * h 
    total += min(l,w,h)

r = 0
for x in input:
    l,w,h = x
    r += l*w*h
    mx = max_index(x)
    for i, v in enumerate(x):
        if i != mx:
            r += 2 * v

print(r)
