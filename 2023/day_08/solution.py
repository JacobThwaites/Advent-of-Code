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

# Part 2

a_nodes = [n for n in network if n.endswith('A')]
distances = []
for curr in a_nodes:
    instruction_index = 0
    first_z = None
    steps = 0
    distances_to_next_z = []
    while True:
        while steps == 0 or not curr.endswith('Z'):
            steps += 1
            index = 0 if instructions[instruction_index] == 'L' else 1
            instruction_index += 1
            if instruction_index >= len(instructions):
                instruction_index = 0
            curr = network[curr][index]
        
        distances_to_next_z.append(steps)
        if not first_z:
            first_z = curr
            steps = 0
        elif curr == first_z:
            break
    
    distances.append(distances_to_next_z)

print(distances)

distances = [d[0] for d in distances]

lcm = math.lcm(*distances)
print(lcm)
