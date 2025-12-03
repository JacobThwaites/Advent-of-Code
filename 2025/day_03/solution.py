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
    filename ='./test.txt'
    with open(filename, 'r') as file:
        input = []
        for line in file:
            line = line.replace('\n', '')
            input.append(line)

        return input

input = get_input()
# [print(row) for row in input]


def max_first(row):
    mx, index = 0,0
    for i, num in enumerate(row[:-1]):
        if int(num) > mx:
            mx = int(num)
            index = i

    return index


assert max_first('987654321111111') == 0
assert max_first('123') == 1

ans = 0
for row in input:
    first_index = max_first(row)
    first_digit = row[first_index]
    second_digit = max([int(n) for n in row[first_index+1:]])
    joltage = int(f'{first_digit}{second_digit}')
    ans += joltage

# print(ans)

# Part 2

def find_next(row: str, starting_index: int, remaining: int) -> int:
    mx = 0
    index = starting_index
    i = starting_index

    while i < len(row) - (remaining - 1):
        num = row[i]
        if int(num) > mx:
            mx = int(num)
            index = i

        i += 1

    return index

assert find_next('234234234234278',0, 12) == 2

def find_num(row: str) -> int:
    remaining = 12
    s = ''
    index = 0

    while remaining > 0:
        index = find_next(row, index, remaining)
        s += str(row[index])

        index += 1
        remaining -= 1

    return int(s)


assert find_num('987654321111111') == 987654321111
assert find_num('818181911112111') == 888911112111
assert find_num("234234234234278") == 434234234278

ans = 0

for row in input:
    ans += find_num(row)

print(ans)
