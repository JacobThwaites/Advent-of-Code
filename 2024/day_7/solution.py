import sys
import math
import bisect
import re
from math import gcd,floor,sqrt,log, prod
from collections import defaultdict as dd
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
            test_value, remaining = line.split(': ')
            input.append([int(test_value), [int(n) for n in remaining.split(' ')]])
        return input 

input = get_input()
# [print(row) for row in input]

def is_valid(target, nums, curr):
    if len(nums) == 0:
        return int(curr) == target
    
    num = nums.pop(0)
    
    if curr * num <= target:
        curr *= num
        if is_valid(target, nums.copy(), curr):
            return True
        curr /= num
    
    if curr + num <= target:
        curr += num
        if is_valid(target, nums, curr):
            return True
        
    return False
        
# total = 0
# for test_value, remaining in input:
#     if is_valid(test_value, remaining, 0):
#         total += test_value

# print(total)

# Part 2

def is_valid(target, nums, curr=0):
    if len(nums) == 0:
        return int(curr) == target

    num = nums.pop(0)

    if curr * num <= target:
        curr *= num
        if is_valid(target, nums.copy(), curr):
            return True
        curr /= num

    if curr + num <= target:
        curr += num
        if is_valid(target, nums.copy(), curr):
            return True
        curr -= num
       
    joined = int(f'{int(curr)}{int(num)}')
    if joined <= target:
        curr = joined
        if is_valid(target, nums.copy(), curr):
            return True

    return False

total = 0
for test_value, remaining in input:
    if is_valid(test_value, remaining):
        total += test_value
print(total)