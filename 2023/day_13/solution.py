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
        content = file.read()
        patterns = content.split('\n\n')
        patterns = [p.split('\n') for p in patterns]
        return patterns

input = get_input()
# print(input)

def recursive_compare(pattern, i, j, total):
    if i < 0 or j >= len(pattern):
        return total
    
    if pattern[i] == pattern[j]:
        return recursive_compare(pattern, i-1, j+1, total+2)
    
    return total


def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        
        above = above[:len(below)]
        below = below[:len(above)]
        
        if above == below:
            return r
        
    return 0

def find_reflection(pattern):
    m = find_mirror(pattern)
    # print(m)
    row_total, col_total = 0,0 
    row_index, col_index = 0,0
    for i, _ in enumerate(pattern[:-1]):
        total = recursive_compare(pattern, i, i+1, 0)
        if total:
            row_total = max(row_total, total)
            row_index = i+1
    
    cols = list(zip(*pattern))
    for i, _ in enumerate(cols[:-1]):
        total = recursive_compare(cols, i, i+1, 0)
        if total:
            col_total = max(col_total, total)
            col_index = i+1

    print('totals')
    print(row_total)
    print(col_total)
    if row_total > col_total:
        return 100 * row_index
    else:
        return col_index


total = 0

total = 0
for pattern in input:  
    total += find_reflection(pattern)
print(total)
# 35561 too high