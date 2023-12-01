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
            line = line.split(' ')
            input.append(line)

        return input 

input = get_input()

total = 1
sm = 1
clock = 0

for cmd in input: 
    print('clock: ' + str(clock))
    print(total)
    if cmd[0] == 'noop': 
        clock += 1
        if clock in [20, 60, 100, 140, 180, 220]:
            sm += total
            # print(clock, sm)
    else:
        if clock + 1 in [20, 60, 100, 140, 180, 220]:
            sm += total
            # print(clock + 1, sm)
        
        v = int(cmd[1])
        print(v)
        total += v
        clock += 2
        if clock in [20, 60, 100, 140, 180, 220]:
            sm += total
            # print(clock + 1, sm)

print(sm)