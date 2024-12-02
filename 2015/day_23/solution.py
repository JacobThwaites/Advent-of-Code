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
    # filename ='./test.txt'
    with open(filename, 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            line = line.replace(',', '')
            line = line.split(' ')
            input.append(line)

        return input 

input = get_input()
# [print(row) for row in input]

register = {
    'a': 1,
    'b': 0
}

i = 0

while i < len(input):
    row = input[i]
    instruction = row[0]
    if instruction == 'hlf':
        register[row[1]] = register[row[1]] / 2
    elif instruction == 'tpl':
        register[row[1]] = register[row[1]] * 3
    elif instruction == 'inc':
        register[row[1]] += 1
    elif instruction == 'jmp':
        offset = row[1]
        if offset[0] == '+':
            i += int(offset[1:])
        else:
            i -= int(offset[1:])
        continue
    elif instruction == 'jie':
        if register[row[1]] % 2 == 0:
            offset = row[2]
            if offset[0] == '+':
                i += int(offset[1:])
            else:
                i -= int(offset[1:])
            continue
    elif instruction == 'jio':
        if register[row[1]] == 1:
            offset = row[2]
            if offset[0] == '+':
                i += int(offset[1:])
            else:
                i -= int(offset[1:])
            continue
    i += 1

print(register)
