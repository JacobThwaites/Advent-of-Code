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
            line = line.replace('%', '')
            line = line.replace('T', '')
            line = line.replace('x', '')
            line = line.replace('y', '')
            line = line.replace('/dev/grid/node-', '')
            line = line.split()
            line[0] = line[0].split('-')
            input.append(line)

        return input

input = get_input()
del input[0]
# [print(row) for row in input]

data = {}
disks = []

for line in input[1:]:
    x = int(line[0][0])
    y = int(line[0][1])
    info = {
        'x': x,
        'y': y,
        'size': int(line[1]),
        'used': int(line[2]),
        'avail': int(line[3]),
        'use': int(line[4])
    }
    data[(x, y)] = info
    disks.append(info)


grid = []

for x in range(25):
    grid.append([])
    for y in range(25):
        grid[x].append(data[(x, y)])

disks.sort(key=lambda x: x['used'])


def find_highest_under(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid]['used'] <= target:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

total = 0
for d in disks:
    index = find_highest_under(disks, d['avail'])

    if not (d['used'] <= d['avail']):
        index += 1

    index -= 1  # to account for single disk with 0 used

    total += index

total += 1 # the single disk with 0 used shouldn't match with itself
print(total)
