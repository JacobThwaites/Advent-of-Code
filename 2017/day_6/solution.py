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
            line = line.replace('\t', ' ')
            line = line.split(' ')
            return [int(t) for t in line]

input = get_input()

def find_max(input):    
    mx = input[0]
    index = 0

    for i, num in enumerate(input[1:]):
        if num > mx:
            mx = num
            index = i + 1
    
    return index

def state_string(input):
    s = ''
    for num in input:
        s += str(num) + ','
    
    return s

def redistribute(input):
    index = find_max(input)
    blocks = input[index]
    input[index] = 0
    
    while blocks > 0:
        index += 1
        if index >= len(input):
            index = 0
        
        input[index] += 1
        blocks -= 1
    

states = {}

curr_state = state_string(input)
cycles = 0
while curr_state not in states:
    states[curr_state] = cycles 
    redistribute(input)
    curr_state = state_string(input)
    cycles += 1
    
print(cycles)

first_seen_cycle = states[curr_state]
loop_size = cycles - first_seen_cycle
print(loop_size)

print(cycles - states[curr_state])