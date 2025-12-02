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


input = 3014387
# input = 5

def rotate_left(bin_str):
    return bin_str[1:] + bin_str[0]

binary_input = bin(input)[2:]
binary_input = int(rotate_left(binary_input), 2)

print(binary_input)


def part2_formula(n):
    # Find largest power of 3 <= n
    power = 1
    while power * 3 <= n:
        power *= 3
    l = n - power
    if l == 0:
        return n
    if l <= power:
        return l
    else:
        return 2 * l - power


input_value = 3014387
print("Part 2 winner (formula):", part2_formula(input_value))
