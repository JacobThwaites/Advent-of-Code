import sys
import math
import bisect
import re
from math import gcd,floor,sqrt,log, prod
from collections import defaultdict as dd, deque
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
# [print(row) for row in input]

total = 0

for row in input:
    x = floor(int(row) / 3) - 2
    total += x

# print(total)


# Part 2

def get_fuel(start):
    if start<= 0:
        return 0
    
    new = max(floor(int(start) / 3) - 2, 0)
    return new + get_fuel(new)

total = sum([get_fuel(int(m)) for m in input])

print(total)
        