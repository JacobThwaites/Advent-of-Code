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
            line = line.split(',')
            return line

input = get_input()

def hash(str):
    curr = 0

    for char in str:
        ascii = ord(char)
        curr += ascii
        curr = curr * 17
        curr = curr % 256
    
    return curr

# total = 0
# for str in input:
#     total += hash(str)

# print(total)



# Part 2 

input = [s.split('=') for s in input]

map = [[] for _ in range(256)]

def add_to_box(input, box):
    label, num = input
    for entry in box:
        if entry[0] == label:
            entry[1] = num
            return 
    
    box.append([label, num])

for i in input:
    if len(i) > 1:
        box = hash(i[0])
        val = (i[0], int(i[1]))
        add_to_box(i, map[box])
    else:
        label = i[0][:-1]
        box = hash(label)

        for j, entry in enumerate(map[box]):
            if entry[0] == label:
                map[box].pop(j)

total = 0

for i, box in enumerate(map):
    for j, lens in enumerate(box):
        total += (i+1) * (j+1) * int(lens[1])

print(total)