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
    with open('./input.txt', 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            input.append(line)

        return input[0]

input = get_input()

def count(nums):
    curr = nums[0]
    total = 1
    counts = []
    for num in nums[1:]:
        if num == curr:
            total += 1
        else:
            counts.append((curr, total))
            curr = num
            total = 1
    counts.append((curr, total))

    return counts

def say(nums):
    s = ''
    for num, count in nums:
        s += str(count) + num

    return s

def count_and_say(str):
    c = count(str)
    return say(c)

s = input

for _ in range(40):
    s = count_and_say(s)

print(len(s))