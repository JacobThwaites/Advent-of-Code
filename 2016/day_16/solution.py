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

input = '00101000101111010'


def flip_bits(n, bit_length):
    return n ^ ((1 << bit_length) - 1)

def reverse(s: str):
    n = int(s, 2)
    bit_length = len(s)

    flipped = flip_bits(n, bit_length)
    return str(bin(flipped)[2:].zfill(bit_length))

def convert(a: str):
    b = a
    b = reverse(b[::-1])
    return f'{a}0{b}'

def generate_checksum(s: str) -> str:
    checksum = ''

    i = 0

    for i in range(0, len(s), 2):
        if s[i] == s[i+1]:
            checksum += '1'
        else:
            checksum += '0'

    if len(checksum) % 2 == 0:
        checksum = generate_checksum(checksum)

    return checksum


assert generate_checksum('110010110100') == '100'

def solve(input):
    target = 272 # Part 1
    target = 35651584 # Part 2

    while len(input) < target:
        input = convert(input)

    input = input[:target]
    checksum = generate_checksum(input)
    print(checksum)

solve(input)

