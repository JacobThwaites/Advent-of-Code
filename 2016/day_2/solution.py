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
            input.append(line)

        return input 

grid = ['123',
        '456',
        '789']
input = get_input()
# print(input)

curr = [1,1]
solution = ""
for instruction in input:
    for dir in instruction: 
        if dir == 'U':
            curr[0] = max(0, curr[0] - 1)
        elif dir == 'D':
            curr[0] = min(len(grid) - 1, curr[0] + 1)
        elif dir == 'L':
            curr[1] = max(0, curr[1] - 1)
        elif dir == 'R':
            curr[1] = min(len(grid[0]) - 1, curr[1] + 1)
    solution = solution + grid[curr[0]][curr[1]]

print(solution)


# Part 2

grid = [
    ['','','1','', ''],
    ['', '2', '3', '4', ''],
    ['5','6','7','8','9'],
    ['', 'A', 'B', 'C', ''],
    ['', '', 'D', '', '']
]

curr = [2, 0]
solution = ""
for instruction in input:
    for dir in instruction:
        if dir == 'U':
            potential = max(0, curr[0] - 1)
            if grid[potential][curr[1]] != '':
                curr[0] = potential
        elif dir == 'D':
            potential = min(len(grid) - 1, curr[0] + 1)
            if grid[potential][curr[1]] != '':
                curr[0] = potential
        elif dir == 'L':
            potential = max(0, curr[1] - 1)
            if grid[curr[0]][potential] != '':
                curr[1] = potential
        elif dir == 'R':
            potential = min(len(grid[0]) - 1, curr[1] + 1)
            if grid[curr[0]][potential] != '':
                curr[1] = potential
    solution = solution + grid[curr[0]][curr[1]]
print(solution)