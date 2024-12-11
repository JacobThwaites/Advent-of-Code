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
    # filename ='./test.txt'
    with open(filename, 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            line = [int(n) for n in list(line)]
            input.append(line)

        return input 

input = get_input()
# [print(row) for row in input]

def get_score(grid, coordinates, start, prev= -1, visited={}):
    x, y = coordinates

    if not (0 <= x < len(grid) and 0 <= y < len(grid[x])):
        return

    if grid[x][y] != prev + 1:
        return

    if (x, y) in visited:
        return

    visited[(x, y)] = True

    if grid[x][y] == 9:
        origins[(x,y)].add(start)
        scores[x][y] += 1
        return

    get_score(grid, (x+1, y), start, prev+1, visited.copy())
    get_score(grid, (x-1, y), start, prev+1, visited.copy())
    get_score(grid, (x, y+1), start, prev+1, visited.copy())
    get_score(grid, (x, y-1), start, prev+1, visited.copy())

scores = [0 for _ in range(len(input[0]))]
scores = [scores.copy() for _ in range(len(input))]
origins = dd(set)

for x, row in enumerate(input):
    for y, val in enumerate(row):
        get_score(input, (x, y), (x, y))

p1 = sum([len(x) for _, x in origins.items()])
print(p1)

p2 = 0
for x, row in enumerate(scores):
    for y, val in enumerate(row):
        p2 += val

print(p2)
