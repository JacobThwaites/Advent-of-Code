import sys
import math
import bisect
import re
from math import gcd,floor,sqrt,log, prod
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
from copy import deepcopy


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
# [print(row) for row in input]

def find_guard(grid):
    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            if val in '^><v':
                return (x,y)
    
    return (-1,-1)

guard_coordinates = find_guard(input)
starting_coordinates = guard_coordinates


def part_1(guard_coordinates, input):
    in_bounds = True

    while in_bounds:
        x,y = guard_coordinates
        if input[x][y] == '^':
            if x == 0:
                input[x][y] = 'X'
                in_bounds = False
                break
            elif input[x-1][y] == '#':
                input[x][y] = '>'
            else:
                input[x][y] = 'X'
                input[x-1][y] = '^'
                guard_coordinates = (x-1, y)
        elif input[x][y] == '>':
            if y == len(input[x]) - 1:
                input[x][y] = 'X'
                in_bounds = False
                break
            elif input[x][y+1] == '#':
                input[x][y] = 'v'
            else:
                input[x][y] = 'X'
                input[x][y+1] = '>'
                guard_coordinates = (x, y+1)
        elif input[x][y] == 'v':
            if x == len(input) - 1:
                input[x][y] = 'X'
                in_bounds = False
                break
            elif input[x+1][y] == '#':
                input[x][y] = '<'
            else:
                input[x][y] = 'X'
                input[x+1][y] = 'v'
                guard_coordinates = (x+1, y)
        elif input[x][y] == '<':
            if y == 0:
                input[x][y] = 'X'
                in_bounds = False
                break
            elif input[x][y-1] == '#':
                input[x][y] = '^'
            else:
                input[x][y] = 'X'
                input[x][y-1] = '<'
                guard_coordinates = (x, y-1)
        else:
            [print(row) for row in input]
            raise Exception(f'non-guard coordinate: {(x, y)}')    

    total = 0

    for x, row in enumerate(input):
        for y, val in enumerate(row):
            if val == 'X':
                total += 1
    
    return total


total = part_1(guard_coordinates, deepcopy(input))
print(total)

# Part 2 
loop_coordinates = {}

def check_for_loop(grid, obstruction_x, obstruction_y, guard_coordinates):
    if grid[obstruction_x][obstruction_y] in '#^<>v':
        return False
    
    grid[obstruction_x][obstruction_y] = '#'
    
    visited = {}
    in_bounds = True
    is_loop = False

    while in_bounds or not is_loop:
        x, y = guard_coordinates
        
        direction = grid[x][y]
        
        if (x, y, direction) in visited:
            is_loop = True
            break
        
        visited[(x,y,direction)] = True
        
        if grid[x][y] == '^':
            if x == 0:
                grid[x][y] = 'X'
                in_bounds = False
                break
            elif grid[x-1][y] == '#':
                grid[x][y] = '>'
            else:
                grid[x][y] = 'X'
                grid[x-1][y] = '^'
                guard_coordinates = (x-1, y)
        elif grid[x][y] == '>':
            if y == len(grid[x]) - 1:
                grid[x][y] = 'X'
                in_bounds = False
                break
            elif grid[x][y+1] == '#':
                grid[x][y] = 'v'
            else:
                grid[x][y] = 'X'
                grid[x][y+1] = '>'
                guard_coordinates = (x, y+1)
        elif grid[x][y] == 'v':
            if x == len(grid) - 1:
                grid[x][y] = 'X'
                in_bounds = False
                break
            elif grid[x+1][y] == '#':
                grid[x][y] = '<'
            else:
                grid[x][y] = 'X'
                grid[x+1][y] = 'v'
                guard_coordinates = (x+1, y)
        elif grid[x][y] == '<':
            if y == 0:
                grid[x][y] = 'X'
                in_bounds = False
                break
            elif grid[x][y-1] == '#':
                grid[x][y] = '^'
            else:
                grid[x][y] = 'X'
                grid[x][y-1] = '<'
                guard_coordinates = (x, y-1)
        else:
            raise Exception(f'invalid guard coordinates: {x,y}. Grid value for coordinates is {grid[x][y]}')

    grid[obstruction_x][obstruction_y] = '.'

    if is_loop:
        return visited
    
    return False


loops = 0
for x, row in enumerate(input):
    for y, val in enumerate(row):
        loop = check_for_loop(deepcopy(input), x, y,
                              guard_coordinates)
        if loop:
            loops += 1

print(loops)