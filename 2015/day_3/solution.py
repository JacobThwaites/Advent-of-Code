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
            input.append(line)

        return input[0]

input = get_input()


p = dd(int)
p[(0,0)] = 1
c = [0,0]
r = [0,0]

for i, d in enumerate(input):
    if d == '>':
        if i%2==0:
            c[1] += 1
        else:
            r[1] += 1
    elif d == '<':
        if i%2==0:
            c[1] -= 1 
        else: 
            r[1] -= 1
    elif d == '^':
        if i%2==0:
            c[0] -= 1
        else:
            r[0] -= 1
    else: 
        if i%2==0:
            c[0] += 1
        else:
            r[0] += 1
    if i%2==0:
        p[(c[0], c[1])] += 1
    else:
        p[(r[0], [1])] += 1

t = 0
for x in p.values():
    if x >= 1:
        t += 1
print(t)
