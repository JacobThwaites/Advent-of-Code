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

def get_new_direction(vector, grid):
    x, y, direction = vector
    square = grid[x][y]
    if square == '.':
        return direction
    elif square == '/':
        if direction == 'right':
            return 'up'
        elif direction == 'down':
            return 'left'
        elif direction == 'left':
            return 'down'
        elif direction == 'up':
            return 'right'
    elif square == '\\':
        if direction == 'right':
            return 'down'
        elif direction == 'down':
            return 'right'
        elif direction == 'left':
            return 'up'
        elif direction == 'up':
            return 'left'
    elif square == '|':
        if direction in ['up', 'down']:
            return direction 
        elif direction in ['left', 'right']:
            return ['up', 'down']
    elif square == '-':
        if direction in ['left', 'right']:
            return direction
        elif direction in ['up', 'down']:
            return ['left', 'right']

def get_new_coordinates(vector):
    x, y, direction = vector
    if direction == 'right':
        return (x, y+1)
    elif direction == 'left':
        return (x, y-1)
    elif direction == 'down':
        return (x+1, y)
    elif direction == 'up':
        return (x-1, y)
    
energised = {}
previous_vectors = {}
lasers = [(0,-1, 'right')]

while len(lasers):
    to_delete = []
    for i, vector in enumerate(lasers):
        new_coordinates = get_new_coordinates(vector)
        x, y = new_coordinates

        if x < 0 or x >= len(input) or y < 0 or y >= len(input[0]):
            to_delete.append(i)
            continue 

        energised[(x,y)] = True
        new_direction = get_new_direction((x, y, vector[2]), input)

        if isinstance(new_direction, list):
            lasers.append((x,y, new_direction[0]))
            lasers[i] = (x,y, new_direction[1])
        else:
            lasers[i] = (x, y, new_direction)
        
        if lasers[i] in previous_vectors:
            to_delete.append(i)
        else: 
            previous_vectors[lasers[i]] = True

    lasers = [laser for i, laser in enumerate(lasers) if i not in to_delete]

print(len(energised.keys()))