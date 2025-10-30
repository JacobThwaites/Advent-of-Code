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
            if line[0] == '+':
                input.append(int(line[1:]))
            else:
                input.append(int(line))

        return input

input = get_input()

res = 0

for num in input:
    res += num
print(res)

def part_2(nums):
    seen = {0: True}

    curr = 0
    while True:
        for num in nums:
            curr += num
            if curr in seen:
                return curr
            seen[curr] = True


ans = part_2(input)
print(ans)