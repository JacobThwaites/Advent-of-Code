import sys
import math
import bisect
import re
import hashlib
import copy
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
            input.append(list(line))

        return input

input = get_input()

def is_oob(x, y, grid):
    return x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y])

def is_roll(x, y, grid):
    if is_oob(x,y, grid):
        return False

    return grid[y][x] == '@'

def total_adjacent(x, y, grid):
    total = 0

    adjacencies = [
        (x+1, y),
        (x+1, y+1),
        (x+1, y-1),
        (x, y-1),
        (x, y+1),
        (x-1, y),
        (x-1, y+1),
        (x-1, y-1),
    ]

    for x, y in adjacencies:
        if is_roll(x, y, grid):
            total += 1

    return total

ans = 0

for y, row in enumerate(input):
    for x, val in enumerate(row):
        if val == '@' and total_adjacent(x, y, input) < 4:
            ans += 1

# print(ans)

# Part 2

def solve(grid, total=0):
    next_grid = copy.deepcopy(grid)
    total_this_time = 0

    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == '@' and total_adjacent(x, y, grid) < 4:
                next_grid[y][x] = '.'
                total_this_time += 1

    if total_this_time == 0:
        return total

    return solve(next_grid, total+total_this_time)

print(solve(input))