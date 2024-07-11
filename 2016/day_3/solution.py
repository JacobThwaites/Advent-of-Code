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
            line = line.split()
            t = [int(x) for x in line]
            input.append(t)
            # input.append(sorted(t))

        return input 

input = get_input()

valid = 0

for t in input:
    if t[-1] < sum(t[:-1]):
        valid += 1
        
# print(valid)


# Part 2
triangles = []

i = 0
while i < len(input):
    triangles.append(sorted([input[i][0], input[i+1][0], input[i+2][0]]))
    triangles.append(sorted([input[i][1], input[i+1][1], input[i+2][1]]))
    triangles.append(sorted([input[i][2], input[i+1][2], input[i+2][2]]))
    i += 3

valid = 0

for t in triangles:
    if t[-1] < sum(t[:-1]):
        valid += 1

print(valid)
# 1589 too low
