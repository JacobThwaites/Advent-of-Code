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
    filename = './input.txt'
    filename ='./test.txt'
    with open(filename, 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            line = line.split(', ')
            return [int(length) for length in line]

lengths = get_input()
# print(lengths)

curr_pos = 0
skip_size = 0

nums = []


for i in range(5):
    nums.append(i)

for length in lengths:
    end = curr_pos + length
    if end >= len(nums):
        offset = end - len(nums)
    else:
        offset = 0

    subarray = nums[curr_pos:curr_pos+length]

    if offset:
        subarray += nums[:offset]

    curr_pos += length + skip_size
    if curr_pos >= len(nums):
        curr_pos = curr_pos % len(nums)
    skip_size += 1