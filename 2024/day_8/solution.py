import sys
import math
import bisect
import re
from math import gcd,floor,sqrt,log, prod
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br

sys.setrecursionlimit(100000000)

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

mod=1000000007


def get_input():
    filename = './input.txt'
    # filename = './test.txt'
    with open(filename, 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            line = list(line)
            input.append(line)

        return input 

input = get_input()
# [print(row) for row in input]

def calculate_antinodes(grid):
    frequencies = dd(list)
    rows, cols = len(grid), len(grid[0])

    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            if val != '.':
                frequencies[val].append((x, y))

    antinodes = set()

    for positions in frequencies.values():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                dx, dy = x2 - x1, y2 - y1

                a = (x1 - dx, y1 - dy)
                if 0 <= a[0] < rows and 0 <= a[1] < cols:
                    antinodes.add(a)

                b = (x2 + dx, y2 + dy)
                if 0 <= b[0] < rows and 0 <= b[1] < cols:
                    antinodes.add(b)

    return len(antinodes)

# print(calculate_antinodes(input))

# Part 2
def next_antinode(grid, coordinates, distance, direction, antinodes):
    x, y = coordinates
    dx, dy = distance
    
    if direction == 'up':
        next = (x+dx, y+dy)
    else:
        next = (x-dx, y-dy)
    
    if not (0 <= next[0] < len(grid) and 0 <= next[1] < len(grid[0])):
        return
    
    antinodes.add(next)
    next_antinode(grid, next, distance, direction, antinodes)

def calculate_antinodes(grid):
    frequencies = dd(list)

    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            if val != '.':
                frequencies[val].append((x, y))

    antinodes = set()

    for positions in frequencies.values():
        antinodes.update(positions)
        
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                dx, dy = x2 - x1, y2 - y1

                next_antinode(grid, positions[i], (dx, dy), 'up', antinodes)
                next_antinode(grid, positions[i], (dx, dy), 'down', antinodes)

    return len(antinodes)

antinodes = calculate_antinodes(input)
print(antinodes)
