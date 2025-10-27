import sys
import math
import bisect
import re
import hashlib
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

        return input[0]

row1 = list(get_input())

def generate_grid(row1):
    grid = [row1]

    for _ in range(39):
        row = ["" for _ in range(len(row1))]
        grid.append(row)

    return grid

grid = generate_grid(row1)

def is_safe(x, y):
    left = y-1 < 0 or grid[x-1][y-1] == '.'
    center = grid[x-1][y] == '.'
    right = y+1 >= len(grid[x-1]) or grid[x-1][y+1] == '.'

    if (left and center) and not right:
        return False

    if (center and right) and not left:
        return False

    if left and (not center and not right):
        return False

    if right and (not center and not left):
        return False

    return True

for x, row in enumerate(grid):
    if x == 0:
        continue

    for y, _ in enumerate(row):
        if is_safe(x, y):
            row[y] = '.'
        else:
            row[y] = '^'

total = 0
for row in grid:
    for val in row:
        if val == '.':
            total += 1

# print(total)

# Part 2

def is_safe(s: str):
    return s not in ["^^.", ".^^", "^..", "..^"]

total_safe_tiles = 0


prev = ''.join(row1)
for s in prev:
    if s == '.':
        total_safe_tiles += 1

x = 1
while x < 400_000:
    row = ""
    x += 1

    if x % 10_000 == 0:
        print(x)

    for i in range(len(prev)):

        if i == 0:
            s = "." + prev[:2]
        elif i == len(prev) - 1:
            s = prev[-2:] + '.'
        else:
            s = prev[i-1:i+2]

        if is_safe(s):
            row += '.'
            total_safe_tiles += 1
        else:
            row += "^"

    prev = row

print(total_safe_tiles)
