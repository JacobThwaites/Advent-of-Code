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
    # filename = './test.txt'
    with open(filename, 'r') as file:
        instructions = []
        for line in file:
            line = line.strip().split()
            if line[0] == 'rect':
                x, y = map(int, line[1].split('x'))
                instructions.append(['rect', x, y])
            else:
                axis = line[1]
                index = int(line[2].split('=')[1])
                distance = int(line[-1])
                instructions.append(['rotate', axis, index, distance])
        return instructions


instructions = get_input()

screen = [['.' for _ in range(50)] for _ in range(6)]  # actual input
# screen = [['.' for _ in range(7)] for _ in range(3)]     # test input

for ins in instructions:
    if ins[0] == 'rect':
        _, a, b = ins
        for y in range(b):
            for x in range(a):
                screen[y][x] = '#'
    else:
        _, axis, index, distance = ins
        if axis == 'column':
            col = index
            column_values = [screen[r][col] for r in range(len(screen))]
            for r in range(len(screen)):
                screen[(r + distance) % len(screen)][col] = column_values[r]
        else:
            row = index
            screen[row] = screen[row][-distance:] + screen[row][:-distance]

total = sum(row.count('#') for row in screen)
print(total)

for row in screen:
    print(''.join(row))
