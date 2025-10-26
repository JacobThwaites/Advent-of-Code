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
        input = []
        for line in file:
            line = line.replace('\n', '')
            start, end = line.split('-')
            input.append((int(start), int(end)))

        return input

input = get_input()

input.sort(key=lambda x : (x[0], x[1]))

def solve() -> int:
    curr = 0

    for start, end in input:
        if curr < start:
            return curr

        curr = max(curr, end + 1)

    return curr

ans = solve()
print(ans)


def solve_part2() -> int:
    MAX_IP = 4294967295
    curr = 0
    total_allowed = 0

    for start, end in input:
        if curr < start:
            total_allowed += start - curr

        curr = max(curr, end + 1)

    total_allowed += MAX_IP - curr + 1
    return total_allowed

ans = solve_part2()
print(ans)