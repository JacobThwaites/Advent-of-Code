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
    with open('./input.txt', 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            line = list(line)
            line = [int(x) for x in line]
            input.append(line)

        return input 

input = get_input()

coordinates = {}

for x, row in enumerate(input):
    row_max = -1
    for y, num in enumerate(row):
        if row_max == 9: 
            break
        if num > row_max:
            row_max = num
            coordinates[(x,y)] = True

for x, row in enumerate(input):
    row_max = -1
    for y, num in enumerate(reversed(row)):
        if row_max == 9: 
            break
        if num > row_max:
            row_max = num
            coordinates[(x,y)] = True

num_rows = len(input)
num_cols = len(input[0])

for col in range(num_cols):
    col_max = -1
    for row in range(num_rows):
        if col_max == 9:
            break
        num = input[row][col]
        print(num)
        if input[row][col] > col_max:
            col_max = input[row][col]
            coordinates[(row, col)] = True

for col in range(num_cols):
    col_max = -1
    for row in range(num_rows-1, -1, -1):
        if col_max == 9:
            break
        if input[row][col] > col_max:
            col_max = input[row][col]
            coordinates[(row, col)] = True

print(len(coordinates))

#  1852 > target > 1500