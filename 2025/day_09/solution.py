from typing import List, Tuple
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
            line = [int(x) for x in line.split(',')]
            line = (line[0], line[1])
            input.append(line)

        return input

input = get_input()
# [print(row) for row in input]

mx = 0

for x, num1 in enumerate(input):
    for y in range(x+1, len(input)):
        num2 = input[y]
        x_distance = abs(num2[0] - num1[0]) + 1
        y_distance = abs(num2[1] - num1[1]) + 1
        distance = x_distance * y_distance
        mx = max(mx, distance)

# print(mx)

# Part 2


def distance(c1, c2):
    x_distance = abs(c1[0] - c2[0])
    y_distance = abs(c1[1] - c2[1])
    return x_distance * y_distance


# get coordinates in order
coordinates = [input[0]]

while len(coordinates) < len(input):
    prev = coordinates[-1]
    next = None
    max_distance = float('inf')

    for coordinate in input:
        if prev == coordinate or coordinate in coordinates:
            continue

        if coordinate[0] != prev[0] and coordinate[1] != prev[1]:
            continue

        d = distance(prev, coordinate)
        if d < max_distance:
            max_distance = d
            next = coordinate

    coordinates.append(next)

coordinates.append(coordinates[0])


# compressed coordinates

def compress_coordinates(points):
    unique_x = sorted(set(x for x, y in points))
    unique_y = sorted(set(y for x, y in points))

    x_map = {x: i for i, x in enumerate(unique_x)}
    y_map = {y: i for i, y in enumerate(unique_y)}

    compressed_points = [(x_map[x], y_map[y]) for x, y in points]

    reverse_map = {}
    for orig, comp in zip(points, compressed_points):
        reverse_map[comp] = orig

    return compressed_points, reverse_map



compressed, reverse_dict = compress_coordinates(coordinates)

#########


max_x = max(c[0] for c in compressed)
max_y = max(c[1] for c in compressed)


grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

# generate outline
for i in range(1, len(compressed)):
    curr = compressed[i]
    prev = compressed[i-1]

    grid[curr[1]][curr[0]] = '#'
    grid[prev[1]][prev[0]] = '#'

    pointer = [curr[0], curr[1]]

    while pointer[0] != prev[0] or pointer[1] != prev[1]:
        if pointer[0] < prev[0]:
            pointer[0] += 1
        elif pointer[0] > prev[0]:
            pointer[0] -= 1

        if pointer[1] < prev[1]:
            pointer[1] += 1
        elif pointer[1] > prev[1]:
            pointer[1] -= 1


        if grid[pointer[1]][pointer[0]] != '#':
            grid[pointer[1]][pointer[0]] = 'X'


# Fill grid

def fill(x, y, grid):
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
        return

    if grid[y][x] in 'X#':
        return

    grid[y][x] = 'X'

    fill(x+1, y, grid)
    fill(x-1, y, grid)
    fill(x, y+1, grid)
    fill(x, y-1, grid)


fill(compressed[0][0]+1, compressed[0][1] + 1, grid)


def is_valid_rectangle(c1, c2, grid):
    start_x = min(c1[0], c2[0])
    end_x = max(c1[0], c2[0])
    start_y = min(c1[1], c2[1])
    end_y = max(c1[1], c2[1])

    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            if grid[y][x] not in '#X':
                return False

    return True

mx = 0

# for x, c1 in enumerate(input):
#     for y in range(x+1, len(input)):
#         c2 = input[y]

#         if is_valid_rectangle(c1, c2, grid):
#             x_distance = abs(c1[0] - c2[0]) + 1
#             y_distance = abs(c1[1] - c2[1]) + 1
#             distance = x_distance * y_distance
#             mx = max(mx, distance)

max_area = 0
for i, c1 in enumerate(compressed):
    for j in range(i + 1, len(compressed)):
        c2 = compressed[j]
        if is_valid_rectangle(c1, c2, grid):
            orig_c1 = reverse_dict[c1]
            orig_c2 = reverse_dict[c2]
            x_distance = abs(orig_c1[0] - orig_c2[0]) + 1
            y_distance = abs(orig_c1[1] - orig_c2[1]) + 1
            area = x_distance * y_distance
            max_area = max(max_area, area)

print(max_area)