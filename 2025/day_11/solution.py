import sys
import math
import bisect
import re
import hashlib
from math import gcd,floor,sqrt,log, prod
from functools import cache
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
        input = dd(list)
        for line in file:
            line = line.replace('\n', '')
            start, links = line.split(': ')
            links = links.split(' ')
            input[start] = links

        return input

input = get_input()
# [print(k, v) for k, v in input.items()]

def solve(start, end):
    queue = deque([start])
    total = 0

    while queue:
        node = queue.popleft()

        if node == end:
            total += 1
            continue

        for x in input[node]:
            queue.append(x)

    return total

ans = solve('you', 'out')

print(ans)

# Part 2


@cache
def solve2(start, end, seen_dac, seen_fft):
    if start == end:
        return 1 if seen_dac and seen_fft else 0

    new_dac = True if seen_dac or start == 'dac' else False
    new_fft = True if seen_fft or start == 'fft' else False

    total = 0

    for x in input[start]:
        total += solve2(x, end, new_dac, new_fft)

    return total


print(solve2('svr', 'out', False, False))
