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
            line[2] = int(line[2])
            line[len(line) - 1] = int(line[len(line) - 1])
            input.append(line)

        return input 

input = get_input()
# [print(row) for row in input]

def compare_nums(num: int, comparison: str, to_compare: int) -> bool: 
    match comparison:
        case '<':
            return num < to_compare
        case '>':
            return num > to_compare
        case '<=':
            return num <= to_compare
        case ">=":
            return num >= to_compare
        case '!=':
            return num != to_compare
        case "==":
            return num == to_compare
        case _:
            return False
    

nums = {}

highest_ever = float('-inf')

for target, method, value, _, num_to_check, comparison, num_for_comparison in input:
    if target not in nums:
        nums[target] = 0
    if num_to_check not in nums:
        nums[num_to_check] = 0
    
    if compare_nums(nums[num_to_check], comparison, num_for_comparison):
        if method == "dec":
            nums[target] -= value
        else:
            nums[target] += value
        highest_ever = max(highest_ever, nums[target])
            
# print(max(nums.values()))
print(highest_ever)