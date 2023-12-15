import sys
import math
import bisect
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
import json
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
            return json.loads(line)

        return input 

input = get_input()
total = 0

def count_nums(obj):
    global total
    if isinstance(obj, str):
        return 
    
    if isinstance(obj, int):
        total += obj 
        print(total)

    if isinstance(obj, dict):
        for v in obj.values():
            count_nums(v)

    if isinstance(obj, list):
        for entry in obj:
            count_nums(entry)

# count_nums(input)
# print(total)

# Part 2

total = 0

def count_nums(obj):
    global total
    if isinstance(obj, str):
        return 
    
    if isinstance(obj, int):
        total += obj 
        print(total)

    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == 'red' or v == 'red':
                return
        for v in obj.values():
            count_nums(v)

    if isinstance(obj, list):
        for entry in obj:
            count_nums(entry)

count_nums(input)

print(total)