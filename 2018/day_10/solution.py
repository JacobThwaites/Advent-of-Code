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
        coordinates = []
        velocities = []
        for line in file:
            line = line.replace('\n', '')
            line = line.replace('position=', '')
            line = line.replace('velocity=', '')
            position, velocity = line.split('> <')
            position = position.replace('<', '')
            position = position.replace(',', '')
            velocity = velocity.replace('>', '')
            velocity = velocity.replace(',', '')

            posX, posY = position.split()
            velX, velY = velocity.split()
            coordinates.append([int(posX), int(posY)])
            velocities.append([int(velX), int(velY)])

        return [coordinates, velocities]


coordinates, velocities = get_input()

def calculate_bounding_box_area(coordinates):
    xs = [c[0] for c in coordinates]
    ys = [c[1] for c in coordinates]

    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    width = max_x - min_x
    height = max_y - min_y
    return width * height


def generate_grid(coordinates):
    min_x = min(c[0] for c in coordinates)
    max_x = max(c[0] for c in coordinates)
    min_y = min(c[1] for c in coordinates)
    max_y = max(c[1] for c in coordinates)

    grid = []
    for y in range(min_y, max_y + 1):
        row = ''
        for x in range(min_x, max_x + 1):
            if [x, y] in coordinates:
                row += '#'
            else:
                row += '.'
        grid.append(row)

    return grid


bb = calculate_bounding_box_area(coordinates)

seconds = 0

while True:
    seconds += 1
    for i, (x, y) in enumerate(coordinates):
        coordinates[i][0] += velocities[i][0]
        coordinates[i][1] += velocities[i][1]

    new_bb = calculate_bounding_box_area(coordinates)
    if new_bb > bb:
        for i, (x, y) in enumerate(coordinates):
            coordinates[i][0] -= velocities[i][0]
            coordinates[i][1] -= velocities[i][1]
        break
    else:
        bb = new_bb

grid = generate_grid(coordinates)
for row in grid:
    print(row)

# NEXPLRXK
print(seconds-1)