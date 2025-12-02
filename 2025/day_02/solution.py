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
            line = line.split(',')
            for entry in line:
                start, end = entry.split('-')
                input.append((int(start), int(end)))

        return input

input = get_input()
# [print(row) for row in input]

def invalid(num: int) -> bool:
    s = str(num)

    if len(s) % 2 != 0:
        return False

    mid = len(s) // 2

    return s[:mid] == s[mid:]

assert invalid(222) == False
assert invalid(1212) == True
assert invalid(1213) == False


ans = 0
for start, end in input:
    for num in range(start, end+1):
        if invalid(num):
            ans += num

print(ans)

# Part 2

def repeats(num: str, length: int) -> bool:
    start = num[:length]

    curr = length

    while curr < len(num):
        if num[curr:curr+length] != start:
            return False
        curr += length

    return True

assert repeats('1111', 1) == True
assert repeats('1112', 1) == False
assert repeats('1212', 2) == True
assert repeats('1213', 2) == False



def invalid(num: int) -> bool:
    s = str(num)
    x = 1

    while x <= len(s) // 2:
        if repeats(s, x):
            return True
        x += 1

    return False


assert invalid(222) == True
assert invalid(1212) == True
assert invalid(1213) == False


ans = 0

for start, end in input:
    for num in range(start, end+1):
        if invalid(num):
            ans += num

print(ans)
