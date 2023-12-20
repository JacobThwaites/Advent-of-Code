import sys
import math
import bisect
from math import gcd,floor,sqrt,log
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
            line = line.split(' -> ')
            input.append(line)

        return input 

input = get_input()

map = {}

for logic, destination in input:
    map[destination] = logic

def solve(destination):
    if destination.isnumeric():
        return int(destination)
    
    value = map[destination]

    if isinstance(value, int) or value.isnumeric():
        map[destination] = int(value)
    elif 'AND' in value:
        a, b = value.split(' AND ')
        map[destination] = solve(a) & solve(b)
    elif 'OR' in value:
        a, b = value.split(' OR ')
        map[destination] = solve(a) | solve(b)
    elif 'LSHIFT' in value:
        a, b = value.split(' LSHIFT ')
        map[destination] = solve(a) << solve(b)
    elif 'RSHIFT' in value:
        a, b = value.split(' RSHIFT ')
        map[destination] = solve(a) >> solve(b)
    elif 'NOT' in value:
        a = value.replace('NOT ', '')
        map[destination] = ~solve(a) & 0xFFFF
    else:
        map[destination] = solve(value)
    
    return map[destination]

def calculate(destination): 
    if isinstance(map[destination], str):
        map[destination] = solve(destination)
    
    return map[destination]

for logic, destination in input:
    calculate(destination)
print(map['a'])