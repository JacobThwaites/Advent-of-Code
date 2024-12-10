import sys
import math
import bisect
import re
from math import gcd,floor,sqrt,log, prod
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
            return line
            input.append(line)

        return input 

input = get_input()

# print(input)

def generate_diskmap(digits):
    id = 0
    is_files = True

    diskmap = []
    for d in digits:
        if is_files:
            [diskmap.append(id) for _ in range(int(d))]
            id += 1
        else:
            [diskmap.append('.') for _ in range(int(d))]
        is_files = not is_files

    return diskmap

def find_next_space(diskmap, starting_index):
    for i, v in enumerate(diskmap[starting_index:], start=starting_index):
        if v == '.':
            return i
        
    return -1

def reorder_blocks(diskmap):
    space = find_next_space(diskmap, 0)
    end = len(diskmap) - 1
    
    while space < end:
        if diskmap[end] != '.':
            diskmap[space] = diskmap[end]
            diskmap[end] = '.'
            space = find_next_space(diskmap, space)
            
        else:
            end -= 1
    
    return diskmap

diskmap = generate_diskmap(input)
reorder_blocks(diskmap)

total = 0
id = 0
for d in diskmap:
    if d == '.':
        break
    total += (id * d)
    id += 1
        
# print(total)

# Part 2

def find_space_by_size(diskmap, size, end_index):
    curr_length = 0
    
    for i, x in enumerate(diskmap,):
        if i == end_index:
            return False
        
        if x == '.':
            curr_length += 1
            if curr_length == size:
                return (i-size+1, i+1)
        else: curr_length = 0
    
    return False

def find_next_id(diskmap, i):
    while i > 0:
        if diskmap[i] != '.':
            return (diskmap[i], i)
        i -= 1
    
    return None

def find_next_file(diskmap, starting_index):
    id, i = find_next_id(diskmap, starting_index)
    starting_index = i
    while True:
        if diskmap[i] != id:
            return (i+1, starting_index+1)
        
        i -= 1 
    
def print_diskmap(diskmap):
    test = ''

    for x in diskmap:
        test += str(x)
    print(test)
    
    return test

def reorder_blocks(diskmap):
    x, y = find_next_file(diskmap, len(diskmap)-1)
    file_size = y-x
    next_space = find_space_by_size(diskmap, file_size, x)

    while x >0:
        if next_space:
            a, b = next_space
            diskmap[a:a+file_size], diskmap[x:y] = diskmap[x:y], diskmap[a:a+file_size]
        x -=1
        x, y = find_next_file(diskmap, x)
        file_size = y-x
        next_space = find_space_by_size(diskmap, file_size, x)
        
    return diskmap

diskmap = generate_diskmap(input)
reorder_blocks(diskmap)

total = 0
for i, d in enumerate(diskmap):
    if d != '.':
        total += (i * d)
print(total)