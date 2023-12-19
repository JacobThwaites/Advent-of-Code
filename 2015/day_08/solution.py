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
    # filename = './test.txt'
    with open(filename, 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            input.append(line)

        return input 

input = get_input()

def count_string_chars(str):
    string_literal_length = len(str)
    in_memory_length = 0
    i = 1
    while i < len(str) - 1:
        char = str[i]
        if char == '\\':
            if str[i+1] in '\\"':
                in_memory_length += 1
                i += 2
            else:
                in_memory_length += 1
                i += 4
        else:
            in_memory_length += 1
            i += 1
    return string_literal_length - in_memory_length

total = sum([count_string_chars(string) for string in input])
# print(total)

# Part 2

def encode(string):
    new = '"'

    for char in string:
        if char in '"\\':
            new += '\\' + char
        else:
            new += char
    
    new += '"'
    return len(new) - len(string)

total_encoded = sum([encode(string) for string in input])
print(total_encoded)