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
# print(input)

start = None

for x, row in enumerate(input):
    for y, val in enumerate(row):
        if val == 'S':
            start = (x, y)
            break

def is_in_bounds(x, y, grid):
    return not (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]))

def is_valid_square(x, y, grid):
    return is_in_bounds(x, y, grid) and grid[x][y] != '#'

def move(grid, starts):
    next_starts = []
    for (x, y) in starts:
        if is_valid_square(x+1, y, grid) and (x+1, y) not in next_starts:
            next_starts.append((x+1, y))
        if is_valid_square(x-1, y, grid) and (x-1, y) not in next_starts:
            next_starts.append((x-1, y))
        if is_valid_square(x, y+1, grid) and (x, y+1) not in next_starts:
            next_starts.append((x, y+1))
        if is_valid_square(x, y-1, grid) and (x, y-1) not in next_starts:
            next_starts.append((x, y-1))

    return next_starts

starts = [start]

for _ in range(64):
    starts = move(input, starts)

print(len(starts))