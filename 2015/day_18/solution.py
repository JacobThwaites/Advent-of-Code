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

def is_on(grid, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
        return 0

    return 1 if grid[x][y] == '#' else 0


def total_neighbours_on(grid, x, y):
    neighbours = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    return sum([is_on(grid, x, y) for x, y in neighbours])

def update_lights(grid):
    new_grid = [['.' for y in range(len(grid[0]))] for _ in range(len(grid))]

    for x, row in enumerate(grid):
        for y, val in enumerate(grid[x]):
            neighbours_on = total_neighbours_on(grid, x, y)
            if val == '#':
                new_grid[x][y] = '#' if neighbours_on in [2,3] else '.'
            else:
                new_grid[x][y] = '#' if neighbours_on == 3 else '.'
    
    return new_grid

grid = input

for _ in range(100):
    grid = update_lights(grid)


total_on = 0

for x, _ in enumerate(grid):
    for x, val in enumerate(grid[x]):
        total_on += 1 if val == '#' else 0 

print(total_on)

# Part 2