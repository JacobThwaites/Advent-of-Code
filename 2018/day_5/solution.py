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
            input.append(line)

        return input[0]

input = get_input()

def are_triggers(a: str, b: str) -> bool:
    chars = [a, b]
    chars.sort()

    return chars[0] == chars[0].upper() and chars[1] == chars[1].lower() and chars[0].lower() == chars[1]

def solve(input):
    stack = []

    for char in input:
        if not stack:
            stack.append(char)
        elif are_triggers(stack[-1], char):
            stack.pop()
        else:
            stack.append(char)

    return len(stack)

ans = solve(input)
print(ans)

# Part 2

def remove_letter(s: str, letter: str) -> str:
    new = ''

    for char in s:
        if char.lower() != letter:
            new += char

    return new


mn = float('inf')
for i in range(97, 123):
    print(chr(i))
    s = remove_letter(input, chr(i))
    mn = min(mn, solve(s))

print(mn)