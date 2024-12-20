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
            line = line.replace('\t', ' ')
            line = line.split(' ')
            line = [int(n) for n in line]
            input.append(line)

        return input 

input = get_input()
# [print(row) for row in input]

total = 0

for row in input:
    total += (max(row) - min(row))

# print(total)

# Part 2

total = 0

def find_divisor(row):
    for i, n in enumerate(row):
        for j in row[i+1:]:
            if n % j == 0 or j % n == 0:
                return int(max(n, j) / min(n, j))

for row in input:
    total += find_divisor(row)

print(total)
                