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
        for line in file:
            line = line.replace('\n', '')
            nums = line.split()
            for i, _ in enumerate(nums):
                nums[i] = int(nums[i])
            return nums


input = get_input()

def generate(input, i):
    node = {'children': [], 'meta': []}
    child_nodes = input[i]
    meta = input[i+1]
    i += 2

    for _ in range(child_nodes):
        child, i = generate(input, i)
        node['children'].append(child)

    node['meta'] = input[i:i + meta]
    i += meta

    return (node, i)

tree, _ = generate(input, 0)

def solve(node):
    total = 0

    for m in node['meta']:
        total += m

    if node['children']:
        for child in node['children']:
            total += solve(child)

    return total

ans = solve(tree)
print(ans)

# Part 2

def solve_2(node):
    total = 0

    if node['children']:
        for m in node['meta']:
            if 1 <= m <= len(node['children']):
                total += solve_2(node['children'][m-1])
    else:
        for m in node['meta']:
            total += m

    return total

ans = solve_2(tree)
print(ans)
