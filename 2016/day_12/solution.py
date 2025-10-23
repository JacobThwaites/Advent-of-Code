import sys
import math
import bisect
import re
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
            line = line.split(' ')
            input.append(line)

        return input

input = get_input()

registers = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0,
}

i = 0

while i < len(input):
    instruction = input[i]
    if instruction[0] == 'inc':
        registers[instruction[1]] += 1
    elif instruction[0] == 'dec':
        registers[instruction[1]] -= 1
    elif instruction[0] == 'cpy':
        val = instruction[1]
        if val in 'abcd':
            val = registers[val]
        else:
            val = int(val)
        registers[instruction[2]] = val
    elif instruction[0] == 'jnz':
        val = instruction[1]
        if val in registers:
            val = registers[val]
        else:
            val = int(val)

        if val != 0:
            i += int(instruction[2])
            continue

    i += 1

for k, v in registers.items():
    print(f'{k}: {v}')
