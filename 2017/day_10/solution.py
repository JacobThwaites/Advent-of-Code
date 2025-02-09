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
    filename = './input.txt'
    filename ='./test.txt'
    with open(filename, 'r') as file: 
        for line in file: 
            line = line.replace('\n', '')
            line = line.split(', ')
            return [int(length) for length in line]

input = get_input()
# [print(row) for row in input]

curr = 0
l = []
skip_size = 0

i = 0

# list_length = 256
list_length = 5
while i < list_length:
    l.append(i)
    i += 1

for length in input:
    # TODO: handle wrapping for reverse
    
    sublist = l[curr:curr + length]
    sublist.reverse()
    l = sublist + l[length:]
    
    curr += length + skip_size
    if curr >= len(l):
        curr = curr % len(l)
    skip_size += 1

    