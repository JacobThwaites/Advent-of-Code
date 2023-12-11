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
    # filename = './input.txt'
    filename ='./test.txt'
    with open(filename, 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            line = list(line)
            input.append(line)

        return input 

input = get_input()

id = 1 

for x, row in enumerate(input):
    for y, col in enumerate(row):
        if col == '#':
            input[x][y] = id
            id += 1

empty_rows = []
empty_cols = []

for x, row in enumerate(input):
    is_empty = True
    for y, col in enumerate(row):
        if col != '.':
            is_empty = False
            break
    
    if is_empty:
        empty_rows.append(x+1)

transposed_input = list(zip(*input))
for y, col in enumerate(transposed_input):
    is_empty = True
    for x, row in enumerate(col):
        if input[x][y] != '.':
            is_empty = False 
            break
    
    if is_empty:
        empty_cols.append(y+1)

# Insert new rows and cols
def expand_matrix(empty_rows, empty_cols, input):
    for empty_row in reversed(empty_rows):
        input.insert(empty_row, ['.' for _ in range(len(input[0]))])

    for empty_col in reversed(empty_cols):
        for row in input:
            row.insert(empty_col, '.')

# expand_matrix(empty_rows, empty_cols, input)

# Get new coordinates
coordinates = []
for x, row in enumerate(input):
    for y, col in enumerate(row):
        if col != '.':
            coordinates.append((x,y))

sum_shortest_paths = 0
for i, c in enumerate(coordinates):
    for j in range(i+1, len(coordinates), 1):
        row_distance = coordinates[j][0] - coordinates[i][0]
        column_distance = abs(coordinates[j][1] - coordinates[i][1])
        sum_shortest_paths += row_distance + column_distance

# print(sum_shortest_paths)


# Part 2
for row in input:
    print(row)