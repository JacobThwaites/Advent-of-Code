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
        for line in file: 
            line = line.replace('\n', '')
            return line.split(', ')

input = get_input()
# print(input)

directions = ['N', 'E', 'S', 'W']
direction_index = 0
coordinates = [0,0]

visited = {}

for instruction in input:
    turn = instruction[0]
    distance = int(instruction[1:])
    if turn == 'L':
        direction_index = (direction_index - 1) % len(directions)
    else:  
        direction_index = (direction_index + 1) % len(directions)
    
    direction = directions[direction_index]
    if direction == 'N':
        for x in range(1, distance+1):
            coordinates[1] -= 1
            if (coordinates[0], coordinates[1]) in visited:
                print(abs(coordinates[0]) + abs(coordinates[1]))
                sys.exit()
            else:
                visited[(coordinates[0], coordinates[1])] = True
    elif direction == 'S':
        for x in range(1, distance+1):
            coordinates[1] += 1
            if (coordinates[0], coordinates[1]) in visited:
                print(abs(coordinates[0]) + abs(coordinates[1]))
                sys.exit()
            else:
                visited[(coordinates[0], coordinates[1])] = True
    elif direction == 'E':
        for x in range(1, distance+1):
            coordinates[0] += 1
            if (coordinates[0], coordinates[1]) in visited:
                print(abs(coordinates[0]) + abs(coordinates[1]))
                sys.exit()
            else:
                visited[(coordinates[0], coordinates[1])] = True
    elif direction == 'W':
        for x in range(1, distance+1):
            coordinates[0] -= 1
            if (coordinates[0], coordinates[1]) in visited:
                print(abs(coordinates[0]) + abs(coordinates[1]))
                sys.exit()
            else:
                visited[(coordinates[0], coordinates[1])] = True
    
# print(abs(coordinates[0])+ abs(coordinates[1]))
# print(sum(coordinates))
# 215: too high