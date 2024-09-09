import sys
import math
import bisect
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br

sys.setrecursionlimit(100000000)


def ceil(x): return int(x) if (x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if (x % d == 0) else x//d+1


mod = 1000000007


def get_input():
    filename = './input.txt'
    # filename = './test.txt'
    with open(filename, 'r') as file:
        input = []
        for line in file:
            return line
            line = line.replace('\n', '')
            return line
            input.append(line)

        return input


input = get_input()
# print(input)

total = 0

for i, num in enumerate(input):
    if i == len(input) - 1:
        if int(input[i]) == int(input[0]):
            total += int(input[i])
    elif int(num) == int(input[i+1]):
        total += int(num)
        
# print(total)

# Part 2

total = 0

for i, num in enumerate(input):
    comparison = int(i + ((len(input)) / 2))
    if comparison > len(input) - 1:
        comparison -= len(input)

    if int(input[i]) == int(input[comparison]):
        total += int(num)

print(total)
