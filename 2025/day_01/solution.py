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
            d = line[0]
            num = int(line[1:])
            input.append((d, num))

        return input

input = get_input()


curr = 50
ans = 0
for d, num in input:
    if d == 'L':
        curr -= num
    else:
        curr += num

    curr %= 100

    if curr == 0:
        ans += 1

print(ans)

# Part 2

curr = 50
ans = 0
for d, num in input:
    for _ in range(num):
        if d == "L":
            curr -= 1
            if curr == 0:
                ans += 1
            elif curr < 0:
                curr = 99
        elif d == 'R':
            curr += 1
            if curr == 100:
                ans += 1
                curr = 0

print(ans)