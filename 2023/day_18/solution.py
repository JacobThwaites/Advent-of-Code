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
            line = line.replace('(', '')
            line = line.replace(')', '')
            line = line.split(' ')
            input.append([line[0], int(line[1]), line[2]])

        return input 

input = get_input()
# print(input)

max_x, max_y = 0,0
min_x, min_y = 0,0
curr = [0,0]

for direction, distance, colour in input:
    if direction == 'U':
        curr[0] -= distance
    elif direction == 'D':
        curr[0] += distance
    elif direction == 'R':
        curr[1] += distance
    elif direction == 'L':
        curr[1] -= distance

    max_x = max(max_x, curr[0])
    max_y = max(max_y, curr[1])
    min_x = min(min_x, curr[0])
    min_y = min(min_y, curr[1])

curr[0] = abs(min_x)
curr[1] = abs(min_y)

grid = [['.' for y in range(min_y,max_y + 1)] for _ in range(min_x, max_x + 1)]

for direction, distance, colour in input:
    x, y = curr[0], curr[1]
    if direction == 'U':
        for i in range(1, distance + 1):
            grid[x-i][y] = '#' 

        curr[0] -= distance
    elif direction == 'D':
        for i in range(1, distance + 1):
            grid[x+i][y] = '#' 

        curr[0] += distance
    elif direction == 'R':
        for i in range(1, distance + 1):
            grid[x][y+i] = '#' 

        curr[1] += distance
    elif direction == 'L':
        for i in range(1, distance + 1):
            grid[x][y-i] = '#' 

        curr[1] -= distance

def flood_fill(grid, starting_coordinates, fill):
    x, y = starting_coordinates
    starting_colour = grid[x][y]
    visited = {}

    stack = [(x, y)] 

    while stack:
        x, y = stack.pop(0)
        if next in visited:
            continue

        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
            continue 

        if grid[x][y] != starting_colour:
            continue
        
        visited[(x, y)] = True 
        grid[x][y] = fill

        stack.append((x+1, y))
        stack.append((x-1, y))
        stack.append((x, y+1))
        stack.append((x, y-1))

fill_coordinates = (1, 1)
fill_coordinates = (curr[0]+1, curr[1]+1)
flood_fill(grid, fill_coordinates, '#')

total = 0
for row in grid:
    for val in row:
        if val == '#':
            total += 1

print(total)