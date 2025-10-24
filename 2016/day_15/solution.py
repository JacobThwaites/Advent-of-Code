import sys
import math
import bisect
import re
import hashlib
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
            line = line.replace('#', '')
            line = line.replace('time=', '')
            line = line.replace('.', '')
            line = line.replace(',', '')
            line = line.split(' ')
            data = {
                'id': int(line[1]),
                'total_positions': int(line[3]),
                'curr_position': int(line[-1])
            }
            input.append(data)

        return input

input = get_input()


def generate_discs():
    discs = {}

    for disc in input:
        discs[disc['id']] = disc.copy()

    return discs


discs = generate_discs()

def rotate_discs(discs):
    for disc in discs.values():
        disc['curr_position'] += 1
        if disc['curr_position'] >= disc['total_positions']:
            disc['curr_position'] = 0


def is_time_valid(time):

    for disc in discs.values():
        if (disc['curr_position'] + time + disc['id']) % disc['total_positions'] != 0:
            return False

    return True

time = 0
while True:
    if is_time_valid(time):
        print(time)
        break

    time += 1

# Part 2
new_id = max(disc['id'] for disc in discs.values()) + 1

discs[new_id] = {'id': new_id, 'curr_position': 0, 'total_positions': 11}

time = 0
while True:
    if is_time_valid(time):
        print(time)
        break

    time += 1
