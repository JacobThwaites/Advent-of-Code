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
            line = list(line)
            input.append(line)

        return input 

input = get_input()

def get_new_coordinates(char, curr_direction, x, y):
    if char == '|':
        if curr_direction == 'north':
            return (x-1, y), 'north'
        elif curr_direction =='south':
            return (x+1,y), 'south'
    elif char == '-':
        if curr_direction == 'east':
            return (x, y+1), 'east'
        elif curr_direction == 'west':
            return (x,y-1), 'west'
    elif char == 'L':
        if curr_direction == 'south':
            return (x, y+1), 'east'
        elif curr_direction == 'west':
            return (x-1, y), 'north'
    elif char == 'J':
        if curr_direction == 'south':
            return (x,y-1), 'west'
        elif curr_direction == 'east':
            return (x-1, y), 'north'
    elif char == '7':
        if curr_direction == 'east':
            return (x+1, y), 'south'
        elif curr_direction == 'north':
            return (x,y-1), 'west'
    elif char == 'F':
        if curr_direction == 'north':
            return (x,y+1), 'east'
        elif curr_direction == 'west':
            return (x+1, y), 'south'
    else:
        return None
    
def find_start(input):
    for x, line in enumerate(input):
        for y, char in enumerate(line):
            if char == 'S':
                return (x,y)


def get_loop_coordinates(input):
    start = find_start(input)

    def dfs(coordinates, direction, path):
        x, y = coordinates[0], coordinates[1]

        if x < 0 or x >= len(input) or y < 0 or y >= len(input[0]):
            return
        
        if input[x][y] == 'S':
            return path

        curr_square = input[x][y]
        res = get_new_coordinates(curr_square, direction, x, y)

        if not res:
            return 
        
        new_coordinates, new_direction = res
        path.append(new_coordinates)

        return dfs(new_coordinates, new_direction, path)


    north_path = dfs((start[0]-1, start[1]), 'north', [])
    if north_path:
        return north_path
    south_path = dfs((start[0]+1, start[1]), 'south', [])
    if south_path:
        return south_path
    east_path = dfs((start[0], start[1]+1), 'east', [])
    if east_path:
        return east_path
    west_path = dfs((start[0], start[1]-1), 'west', [])
    if west_path:
        return west_path

loop_coordinates = get_loop_coordinates(input)
print(ceil(len(loop_coordinates) / 2))

# Part 2


# print(loop_coordinates)