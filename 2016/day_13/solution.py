import sys
import math
import bisect
import re
from math import gcd,floor,sqrt,log, prod
from collections import defaultdict as dd, deque
from bisect import bisect_left as bl, bisect_right as br

sys.setrecursionlimit(100000000)

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

mod=1000000007


# TEST VALUES
# target = (7,4)
# favourite_number = 10
# GRID_SIZE = 10

target = (31, 39)
favourite_number = 1364
GRID_SIZE = 39

def is_wall(x, y):
    if x < 0 or y < 0:
        return True

    a = x*x + 3*x + 2*x*y + y + y*y
    a += favourite_number
    binary_repr = bin(a)
    total_ones = binary_repr.count('1')

    return total_ones % 2 != 0

distances = dd(int)

def solve():
    visited = {}
    queue = [[(1,1), 0]]

    while queue:
        coordinates, distance_travelled = queue.pop(0)

        if coordinates in visited:
            continue

        visited[coordinates] = True

        x, y = coordinates

        if is_wall(x, y):
            continue

        if x == target[0] and y == target[1]:
            return distance_travelled

        queue.append([(x+1, y), distance_travelled + 1])
        queue.append([(x-1, y), distance_travelled + 1])
        queue.append([(x, y+1), distance_travelled + 1])
        queue.append([(x, y-1), distance_travelled + 1])

part1 = solve()

print(part1)

# Part 2

def solve_part_2():
    within_50 = {}
    visited = {}
    queue = [[(1, 1), 0]]

    while queue:
        coordinates, distance_travelled = queue.pop(0)

        if distance_travelled > 50:
            continue

        if coordinates in visited:
            continue

        visited[coordinates] = True

        x, y = coordinates

        if is_wall(x, y):
            continue

        within_50[coordinates] = True

        queue.append([(x+1, y), distance_travelled + 1])
        queue.append([(x-1, y), distance_travelled + 1])
        queue.append([(x, y+1), distance_travelled + 1])
        queue.append([(x, y-1), distance_travelled + 1])

    return len(within_50)

print(solve_part_2())