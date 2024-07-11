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
            input.append(line)

        return input 

input = get_input()

counts = {}

for i, v in enumerate(input[0]):
    counts[i] = dd(int)

for row in input:
    for i, c in enumerate(row):
        counts[i][c] += 1

# print(counts)
code = ''
for i, col in counts.items():
    ordered = sorted(col.items(), key= lambda x: (x[1], x[0]), reverse=True)
    mx = ordered[0][0]
    code = code + mx

print(code)

# Part 2

code = ''
for i, col in counts.items():
    ordered = sorted(col.items(), key=lambda x: (x[1], x[0]))
    mx = ordered[0][0]
    code = code + mx

print(code)
