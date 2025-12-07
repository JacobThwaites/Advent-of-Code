import sys
import math
import bisect
import re
import hashlib
from math import gcd,floor,sqrt,log, prod
from collections import defaultdict as dd, deque
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

def find_start(input):
    for i, v in enumerate(input[0]):
        if v == 'S':
            return (i, 0)


start = find_start(input)

beams = {}
beams[start] = True
splits = 0

while beams:
    new_beams = {}
    for i, beam in enumerate(beams):
        beam = (beam[0], beam[1] + 1)

        x, y = beam[0], beam[1]

        if y >= len(input) or x >= len(input[y]) or x < 0:
            continue

        if input[y][x] == '^':
            splits += 1
            new_beams[(x-1, y)] = True
            new_beams[(x+1, y)] = True
        else:
            new_beams[beam] = True

    beams = new_beams

# print(splits)

# Part 2

beams = {start: 1}
ans = 0

while beams:
    next_beams = dd(int)

    for (x, y), total in beams.items():
        new_x, new_y = x, y + 1

        if new_y >= len(input) or new_x < 0 or new_x >= len(input[new_y]):
            ans += total
            continue

        if input[new_y][new_x] == '^':
            left = (new_x - 1, new_y)
            right = (new_x + 1, new_y)
            next_beams[left] += total
            next_beams[right] += total
        else:
            next_beams[(new_x, new_y)] += total

    beams = next_beams

print(ans)
