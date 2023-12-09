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
            line = line.split(' = ')
            input.append(line)

        return input 

input = get_input()

instructions = ''

nodes = []

network = {}

for i, line in enumerate(input): 
    if i == 0:
        instructions = line[0]
    elif line == ['']:
        continue
    else:
        line[1] = line[1].replace('(','')
        line[1] = line[1].replace(')','')
        location = line[0]
        l, r = line[1].split(', ')
        network[line[0]] = (l, r)

start = network['AAA']

is_end = False
steps = 0

while not is_end:
    for direction in instructions:
        steps += 1
        if direction == 'L':
            if start[0] == 'ZZZ':
                is_end = True 
                break
            start = network[start[0]]
        else:
            if start[1] == 'ZZZ':
                is_end = True 
                break
            start = network[start[1]]

# print(steps)


# Part 2

nodes_ending_with_a = []
for n in network.keys():
    if n[-1] == 'A':
        nodes_ending_with_a.append(n)

starts = nodes_ending_with_a

while True:
    distances_to_next_z = []
    steps = 0

    while len(distances_to_next_z) > 6:
        for instruction in instructions:
            pass
