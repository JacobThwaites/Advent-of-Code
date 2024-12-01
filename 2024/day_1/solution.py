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
    # filename ='./test.txt'
    with open(filename, 'r') as file: 
        input = []
        left = []
        right = []
        for line in file: 
            line = line.replace('\n', '')
            l, r = line.split('   ')
            left.append(int(l))
            right.append(int(r))

        input = [left, right]
        return input 

input = get_input()
# [print(row) for row in input]


def min_index(arr):
    index = 0
    mn = float('inf')

    for i, v in enumerate(arr):
        if v < mn:
            mn = v
            index = i

    return index

left, right = input[0], input[1]

total = 0
# while len(left) > 0:
#     left_index = min_index(left)
#     right_index = min_index(right)
    
#     distance = max(abs(left[left_index]), abs(
#         right[right_index])) - min(abs(left[left_index]), abs(right[right_index]))
#     total += distance
#     left.pop(left_index)
#     right.pop(right_index)

# print(total)

# Part 2

left, right = input[0], input[1]

counts = dd(int)
left_nums = {}

for num in left:
    left_nums[num] = True

for num in right:
    if num in left_nums:
        counts[num] += 1
    
total = 0    
for num in left:
    total += (num * counts[num])
        
print(total)