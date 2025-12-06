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
    filename ='./test.txt'
    with open(filename, 'r') as file:
        input = []

        for line in file:
            line = line.split()
            if len(input) < len(line):
                input = [[] for _ in range(len(line))]

            for i, x in enumerate(line):
                if x not in '*+':
                    x = int(x)
                input[i].append(x)

        return input

input = get_input()
# [print(row) for row in input]

ans = 0

for row in input:
    if row[-1] == '+':
        ans += sum(row[:-1])
    else:
        ans += prod(row[:-1])

print(ans)


# Part 2

def get_columns():
    filename = "./input.txt"
    # filename = "./test.txt"
    with open(filename, "r") as f:
        rows = [line.rstrip("\n") for line in f]

    max_len = max(len(row) for row in rows)
    rows = [row.ljust(max_len) for row in rows]

    columns = []
    for c in range(max_len):
        col = [row[c] for row in rows]
        columns.append(col)

    return columns

cols = get_columns()

def is_empty(col):
    for v in col:
        if v != ' ':
            return False

    return True

calcs = []

curr = []
curr_type = None
for c in cols:
    if is_empty(c):
        calcs.append((curr, curr_type))
        curr = []
        curr_type = None
        continue

    if c[-1] in '+*':
        curr_type = c[-1]

    num = int(''.join(c[:-1]))
    curr.append(num)

if curr_type != None:
    calcs.append((curr, curr_type))


ans = 0
for nums, calc in calcs:
    if calc == '+':
        ans += sum(nums)
    else:
        ans += prod(nums)

print(ans)
