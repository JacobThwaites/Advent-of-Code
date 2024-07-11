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
    filename ='./test.txt'
    with open(filename, 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            line = line.split(' ')
            if line[0] == 'rect':
                x, y = line[1].split('x')
                input.append([line[0], int(x), int(y)])
                continue
            
            input.append([line[0], line[1], int(line[2][2]), int(line[-1])])

        return input 

input = get_input()
# [print(row) for row in input]

screen = [['.' for _ in range(50)] for _ in range(6)]
screen = [['.' for _ in range(7)] for _ in range(3)]

for instruction in input:
    if instruction[0] == 'rect':
        for y in range(instruction[2]):
            for x in range(instruction[1]):
                screen[y][x] = '#'
    else:
        if instruction[1] == 'column':
            new_on = {}
            y = instruction[2]
            distance = instruction[3]
            for x, row in enumerate(screen):
                if row[y] == '#':
                    new_coordinate = (y + distance) % len(screen)
                    new_on[(x + distance) % len(screen)] = True
            
            for x, row in enumerate(screen):
                screen[x][y] = '#' if x in new_on else '.'
        else:
            x = instruction[2]
            distance = instruction[3]
            new_on = {}
            for i, c in enumerate(screen[x]):
                if c == '#':
                    new_on[(i + distance) % len(screen[x])] = True
            
            for i, c in enumerate(screen[x]):
                screen[x][i] = '#' if i in new_on else '.'
    
total = 0

for row in screen:
    for val in row: 
        if val == '#':
            total += 1
print(total)
# 105 - too low