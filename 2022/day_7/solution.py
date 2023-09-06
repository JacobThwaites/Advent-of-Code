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
            command = line.split(' ')
            input.append(command)

        return input 

input = get_input()

# Generate directory
outer = {}
is_listing = False
pointer = outer

for command in input:
    if command[0] == '$':
        if command[1] == 'ls':
            is_listing = True
        elif command[1] == 'cd':
            if command[2] == '..':
                pointer = pointer['parent']
            elif command[2] == '/':
                pointer = outer
            else:
                parent = pointer
                pointer = pointer[command[2]]
                pointer['parent'] = parent
    elif command[0] == 'dir':
        dir_name = command[1]
        pointer[dir_name] = {}
    else:
        file_name = command[1]
        pointer[file_name] = int(command[0])


sm = 0

def count_directory_memory(directory):
    global sm
    memory = 0
    for k, v in directory.items():
        if k == 'parent':
            continue
        elif isinstance(v, int):
            memory += v
        else :
            memory += count_directory_memory(v)


    if memory <= 100000:
        sm += memory

    return memory

total_memory = count_directory_memory(outer)

# Part 2 

available =  70000000
unused = available - total_memory
min_unused = 30000000

target = min_unused - unused
smallest = float('inf')

def find_smallest(directory):
    global smallest
    global target

    memory = 0
    for k, v in directory.items():
        if k == 'parent':
            continue
        elif isinstance(v, int):
            memory += v
        else:
            memory += find_smallest(v)

    if memory >= target:
        smallest = min(smallest, memory)

    return memory

find_smallest(outer)
print(smallest)