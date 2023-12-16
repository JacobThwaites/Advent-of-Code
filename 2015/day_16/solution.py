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
    with open(filename, 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            line = line.replace(':', '')
            line = line.replace(',', '')
            line = line.split(' ')
            s = [line[1], (line[2], int(line[3])), (line[4], int(line[5])), (line[6], int(line[7]))]
            input.append(s)

        return input 

input = get_input()

values = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

sues = dd(dd)

for num, (val1, v1_total), (val2, v2_total), (val3, v3_total) in input:
    sues[num][val1] = v1_total
    sues[num][val2] = v2_total
    sues[num][val3] = v3_total

# for name, total in values.items():
#     for num, s in sues.items():
#         if name in s and s[name] != total:
#             s['X'] = False


# for num, s in sues.items():
#     if 'X' not in s:
#         print(num)

# Part 2

for name, total in values.items():
    for num, s in sues.items():
        if name in s:
            if name in ['cats', 'trees']:
                if s[name] <= total:
                    s['X'] = False
            elif name in ['pomeranians', 'goldfish']:
                if s[name] >= total:
                    s['X'] = False
            elif s[name] != total:
                s['X'] = False

for num, s in sues.items():
    if 'X' not in s:
        print(num)