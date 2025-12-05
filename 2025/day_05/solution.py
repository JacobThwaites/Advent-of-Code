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
        is_ranges = True
        ranges = []
        ids = []
        input = []
        for line in file:
            if line == '\n':
                is_ranges = False
                continue
            elif is_ranges:
                start, end = line.split('-')
                ranges.append([int(start), int(end)])
            else:
                ids.append(int(line))
            input.append(line)

        return [ranges, ids]

ranges, ids = get_input()

ans = 0

def is_fresh(id, ranges):
    for start, end in ranges:
        if start <= id <= end:
            return True

    return False

for id in ids:
    if is_fresh(id, ranges):
        ans += 1

print(ans)


# Part 2

def merge_ranges(ranges):
    ranges.sort(key = lambda r: r[0])
    new_ranges = []

    for range in ranges:
        is_merged = False
        for i, (start, end) in enumerate(new_ranges):
            if start <= range[0] <= end:
                new_ranges[i][1] = max(range[1], end)
                is_merged = True
                break

        if not is_merged:
            new_ranges.append(range)

    return new_ranges

ranges = merge_ranges(ranges)

total = sum((end - start + 1) for start, end in ranges)
print(total)
