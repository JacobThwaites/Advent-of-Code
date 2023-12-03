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
            input.append(line)

        return input 

input = get_input()

def is_part(s):
    return s != '.' and not s.isnumeric()

# 1, 1
def is_adjacent_to_part(x, y, input):
    # Check row above
    if x > 0:
        # 0, 1
        if is_part(input[x-1][y]):
            return True
        #0, 0
        if y > 0 and is_part(input[x-1][y-1]):
            return True
        # 0, 2
        if y < len(input[x]) - 2 and is_part(input[x-1][y+1]):
            return True
    # Check current row
    if y > 0:
        # 1, 0
        if is_part(input[x][y-1]):
            return True
        # 1, 2
        if y < len(input[x]) - 2 and is_part(input[x][y+1]):
            return True
    # Check row below 
    if x < len(input) - 2:
        #2, 0
        if y > 0 and is_part(input[x+1][y-1]):
            return True
        #2, 1
        if is_part(input[x+1][y]):
            return True
        # 2, 2
        if y < len(input[x]) - 2 and is_part(input[x+1][y+1]):
            return True

    return False

part_number_sum = 0

for x, row in enumerate(input):
    curr_num = ''
    is_valid = False 
    for y, val in enumerate(input[x]):
        if val.isnumeric():
            curr_num += val
            if is_adjacent_to_part(x, y, input):
                is_valid = True 
        else: 
            if curr_num and is_valid:
                part_number_sum += int(curr_num)
            curr_num = ''
            is_valid = False

    if curr_num and is_valid:
        part_number_sum += int(curr_num)

# print(part_number_sum)

# Part 2

def is_gear(s):
    return s == "*"

gear_numbers = dd(dd)

def add_coordinates_number(x, y, gear_coordinates, input):
    gear_coordinates[(x, y)] = True
    if y > 0 and input[x][y-1].isnumeric() and (x, y-1) not in gear_coordinates:
        add_coordinates_number(x, y-1, gear_coordinates, input)
    if y < len(input[x]) - 1 and input[x][y+1].isnumeric() and (x, y+1) not in gear_coordinates:
        add_coordinates_number(x, y+1, gear_coordinates, input)

def is_adjacent_to_gear(x, y, input):
    # Check row above
    if x > 0:
        # 0, 1
        if is_gear(input[x-1][y]):
            add_coordinates_number(x, y, gear_numbers[(x-1, y)], input)
        #0, 0
        if y > 0 and is_gear(input[x-1][y-1]):
            add_coordinates_number(x, y, gear_numbers[(x-1, y-1)], input)
        # 0, 2
        if y < len(input[x]) - 2 and is_gear(input[x-1][y+1]):
            add_coordinates_number(x, y, gear_numbers[(x-1, y+1)], input)
    # Check current row
    if y > 0:
        # 1, 0
        if is_gear(input[x][y-1]):
            add_coordinates_number(x, y, gear_numbers[(x, y-1)], input)
        # 1, 2
        if y < len(input[x]) - 2 and is_gear(input[x][y+1]):
            add_coordinates_number(x, y, gear_numbers[(x, y+1)], input)
    # Check row below 
    if x < len(input) - 2:
        #2, 0
        if y > 0 and is_gear(input[x+1][y-1]):
            add_coordinates_number(x, y, gear_numbers[(x+1, y-1)], input)
        #2, 1
        if is_gear(input[x+1][y]):
            add_coordinates_number(x, y, gear_numbers[(x+1, y)], input)
        # 2, 2
        if y < len(input[x]) - 2 and is_gear(input[x+1][y+1]):
            add_coordinates_number(x, y, gear_numbers[(x+1, y+1)], input)

for x, row in enumerate(input):
    for y, val in enumerate(row):
        if val.isnumeric():
            is_adjacent_to_gear(x, y, input)

sum_gear_nums = 0

for coordinates in gear_numbers.values():
    gear_nums = []
    curr_num = ''
    for c in sorted(coordinates.keys()):
        curr_num += input[c[0]][c[1]]
        if (c[0], c[1]+1) not in coordinates:
            gear_nums.append(int(curr_num))
            curr_num = ''
    if curr_num:
        gear_nums.append(int(curr_num))
    
    if len(gear_nums) >= 2:
        sum_gear_nums += (gear_nums[0] * gear_nums[1])

print(sum_gear_nums)