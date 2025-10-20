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
    with open(filename, 'r') as file:
        input = []
        for line in file:
            line = line.replace('\n', '')
            line = line.replace('.', '')
            line = line.replace(',', '')
            line = line.split(' ')

            start = int(line[-3])
            end = int(line[-1])
            return (start, end)

        return input

target_x, target_y = get_input()

def calculate_next(curr):
    next = curr * 252533
    return next % 33554393

assert (calculate_next(20151125) == 31916031)

def generate_grid(target_x, target_y):
    curr = 20151125
    grid = [[curr]]

    while len(grid) < target_x + 1 or len(grid[target_x]) < target_y + 1:
        for i, row in enumerate(grid):
            grid[i].append(0)

        grid.append([0])

        i = len(grid) - 1
        while i >= 0:
            curr = calculate_next(curr)
            grid[i][-1] = curr

            i -= 1

    return grid


grid = generate_grid(target_x, target_y)

print(grid[target_x-1][target_y-1])

