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
        for line in file: 
            line = line.replace('\n', '')
            line = line.split(' ')
            line = [int(n) for n in line]
            input.append(line)

        return input 

input = get_input()

def all_nums_zero(nums):
    for n in nums:
        if n != 0:
            return False
    
    return True

def create_diffs(nums):
    diffs = [nums]

    while not all_nums_zero(diffs[-1]):
        prev = diffs[-1]
        diffs.append([])
        for i in range(1, len(prev)):
            diff = prev[i] - prev[i-1]
            diffs[-1].append(diff)
    
    return diffs

diffs = []
for line in input:
    line_diffs = create_diffs(line)
    diffs.append(line_diffs)

def extrapolate_diffs(diffs):
    for d in diffs:
        d.reverse()

        for i in range(1, len(d)):
            nums = d[i]
            c = nums[-1] + d[i-1][-1]
            nums.append(c)
    
    return diffs

# diffs = extrapolate_diffs(diffs)
finals_lists = [d[-1] for d in diffs]
finals = [f[-1] for f in finals_lists]
# print(sum(finals))


# Part 2

print(diffs)

# The same as part 1 but reversing all rows first and using subtraction instead of addition
def extrapolate_bacwards(diffs):
    for d in diffs:
        d.reverse()

        for row in d:
            row.reverse()

        for i in range(1, len(d)):
            nums = d[i]
            c = nums[-1] - d[i-1][-1]
            nums.append(c)
    
    return diffs

backwards_diffs = extrapolate_bacwards(diffs)
finals_lists = [d[-1] for d in backwards_diffs]
finals = [f[-1] for f in finals_lists]
print(sum(finals))