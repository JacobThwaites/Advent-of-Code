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



GRID_SERIAL_NUMBER = 3463
# GRID_SERIAL_NUMBER = 18


def generate_grid():
    grid = [[None for _ in range(300)] for _ in range(300)]
    for x in range(300):
        for y in range(300):
            grid[x][y] = (x+1,y+1)

    return grid

grid = generate_grid()

def hundreds_digit(num: int) -> int:
    s = str(num)
    if len(s) < 3:
        return 0

    return int(s[-3])

def power_level(x, y, serial_number):
    rack_id = x + 10
    power_level = rack_id * (y)
    power_level += serial_number
    power_level *= rack_id
    hundreds = hundreds_digit(power_level)
    power_level = hundreds - 5
    return power_level

assert power_level(3, 5, 8) == 4
assert power_level(122, 79, 57) == -5
assert power_level(217, 196, 39) == 0
assert power_level(101, 153, 71) == 4

for y, col in enumerate(grid):
    for x, _ in enumerate(col):
        p = power_level(x+1, y+1, GRID_SERIAL_NUMBER)
        grid[y][x] = p


def three_by_three(x: int, y: int) -> int:
    if y + 3 >= len(grid) or x + 3 >= len(grid[y]):
        return float('-inf')

    total = 0
    for i in range(y, y+3):
        for j in range(x, x+3):
            total += grid[i][j]

    return total

max_square = float('-inf')
max_coordinates = None

for y, col in enumerate(grid):
    for x, _ in enumerate(col):
        square = three_by_three(x, y)

        if square > max_square:
            max_square = square
            max_coordinates = (x+1,y+1)

# print(max_square)
# print(f'{max_coordinates[0]},{max_coordinates[1]}')


# Part 2


sat = [[0] * (300 + 1) for _ in range(300 + 1)]

for y in range(1, 301):
    for x in range(1, 301):
        p = power_level(x, y, GRID_SERIAL_NUMBER)
        sat[y][x] = p + sat[y-1][x] + sat[y][x-1] - sat[y-1][x-1]


def square_power(x, y, s):
    x2, y2 = x + s - 1, y + s - 1
    return sat[y2][x2] - sat[y-1][x2] - sat[y2][x-1] + sat[y-1][x-1]

GRID_SIZE = 300
best = None
for s in range(1, GRID_SIZE + 1):
    for y in range(1, GRID_SIZE - s + 2):
        for x in range(1, GRID_SIZE - s + 2):
            total = square_power(x, y, s)
            if not best or total > best[0]:
                best = (total,x,y,s)

print(f'{best[1]},{best[2]},{best[3]}')
