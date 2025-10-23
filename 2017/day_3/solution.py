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


target = 368078

def change_direction(curr_direction):
    if curr_direction == 'up':
            return 'left'
    elif curr_direction == 'down':
        return 'right'
    elif curr_direction == 'left':
        return 'down'
    elif curr_direction == 'right':
        return 'up'
    else:
        return "INVALID_DIRECTION"

adjacent_sums = {(0,0): 1}

def calculate_sum(x, y):
    if (x, y) in adjacent_sums:
        return adjacent_sums[(x, y)]

    adjacenies = [
        (x+1, y),
        (x+1, y+1),
        (x+1, y-1),
        (x-1, y),
        (x-1, y+1),
        (x-1, y-1),
        (x, y+1),
        (x, y-1),
    ]

    total = 0
    for a in adjacenies:
        if a in adjacent_sums:
            total += adjacent_sums[a]

    return total

def generate_spiral(target):
    curr_width = 0
    direction = 'right'
    coordinates = [0,0]


    for _ in range(1, target):
        x, y, = coordinates[0], coordinates[1]
        adjacent_sums[(x, y)] = calculate_sum(x, y)
        if adjacent_sums[(x, y)] > target:
            print(f'Part 2: {adjacent_sums[(x, y)]}')
            return

        if direction == 'up':
            coordinates[0] -= 1
            if abs(coordinates[0]) == curr_width:
                direction = change_direction(direction)
        elif direction == 'down':
            coordinates[0] += 1
            if abs(coordinates[0]) == curr_width:
                direction = change_direction(direction)
        elif direction == 'left':
            coordinates[1] -= 1
            if abs(coordinates[1]) == curr_width:
                direction = change_direction(direction)
        elif direction == 'right':
            coordinates[1] += 1
            if abs(coordinates[1]) > curr_width:
                curr_width += 1
                direction = change_direction(direction)
                continue

    return abs(coordinates[0]) + abs(coordinates[1])



# part1 = generate_spiral(target)
# print(part1)

# Part 2
generate_spiral(target)


