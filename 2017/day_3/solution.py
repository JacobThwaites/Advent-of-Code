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
    # filename = './input.txt'
    filename ='./test.txt'
    with open(filename, 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            return int(line)
            input.append(line)

        return input 

input = get_input()
# print(input)
target = 100

def generate_grid(target):
    grid = [[1]]

    direction = 'R'
    coordinates = [0,0]
    count = 0

    try:
        while count < target:
            [print(r) for r in grid]
            print('')
            count += 1
            x,y = coordinates
            if direction == 'R':
                if y == len(grid[x]) - 1:
                    for i, row in enumerate(grid):
                        # grid[]
                        row.append(None)
                    grid[x][y+1] = count
                    direction = 'U'
                else:
                    grid[x][y] = count
                    coordinates = [x, y+1]
            elif direction == 'U':
                if x == 0:
                    grid.insert(0, [None] * len(grid))
                    grid[0][y] = count
                    direction = 'L'
                else: 
                    grid[x][y] = count
                    coordinates = [x-1, y]
            elif direction == 'L':
                if y == 0:
                    for row in grid:
                        row.insert(0, None)
                    direction = 'D'
                    grid[x][y] = count
                else:
                    grid[x][y] = count
                    coordinates = [x, y-1]
            elif direction == 'D':
                if x >= len(grid):
                    grid.append([None] * len(grid[0]))
                    grid[x][y] = count
                    direction = 'R'
                else:
                    grid[x][y] = count
                    coordinates = [x+1, y]
    except Exception as e:
        print(e)
        pass
    
    return grid
    
# grid = generate_grid(target)
# [print(r) for r in grid]


def generate_spiral(target):
    # Calculate necessary grid size (square root rounded up to the next odd integer)
    size = math.ceil(math.sqrt(target))
    if size % 2 == 0:
        size += 1  # Ensure the size is odd to center the spiral

    # Initialize the grid with None
    grid = [[None for _ in range(size)] for _ in range(size)]

    # Start in the center of the grid
    x, y = size // 2, size // 2
    grid[x][y] = 1  # Place the first number

    # Directions: right, up, left, down (cyclical)
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    dir_index = 0  # Start by moving right

    # Step size control for the spiral
    step_size = 1
    current_value = 2  # Start from 2 since 1 is already placed

    while current_value <= target:
        for _ in range(2):  # Repeat twice for each step size (e.g., right & up, then left & down)
            dx, dy = directions[dir_index]  # Get the current direction
            for _ in range(step_size):  # Move step_size steps in the current direction
                if current_value > target:
                    break
                x, y = x + dx, y + dy
                grid[x][y] = current_value
                current_value += 1
            dir_index = (dir_index + 1) % 4 
        step_size += 1

    return grid


target = 368078
spiral = generate_spiral(target)

[print(r) for r in spiral]

def find_index(target, spiral):    
    for x, row in enumerate(spiral):
        for y, val in enumerate(row):
            if val == target:
                return (x, y)
    
    return (-1, -1)
print(len(spiral))
(x1, y1) = find_index(1, spiral)
(x2, y2) = find_index(target, spiral)
            
distance = (x2-x1) + (y2-y1)
print(distance)
# 235 - too low