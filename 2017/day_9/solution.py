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
            return line

        return input 

input = get_input()

# print(input)

def find_score(input):
    depth = 0
    total = 0
    inside_garbage = False
    garbage_chars = 0

    i = 0

    while i < len(input):
        char = input[i]
        if inside_garbage:
            if char == "!": 
                i += 2
                continue
            elif char == ">":
                inside_garbage = False
            else:
                garbage_chars += 1
        
        elif char == "{":
            depth += 1
        elif char == "}":
            total += depth
            depth -= 1
        elif char == "<":
            inside_garbage = True 
        
        i += 1
    
    print(garbage_chars)
    return total
    
# print(find_score('{}'))
# print(find_score('{{{}}}'))
# print(find_score('{{}, {}}'))
# print(find_score('{{{}, {}, {{}}}}'))
# print(find_score('{< a > , < a > , < a > , < a > }'))
# print(find_score('{{ < ab > }, { < ab > }, { < ab > }, { < ab > }}'))
# print(find_score('{{ < !! > }, { < !! > }, { < !! > }, { < !! > }}'))
# print(find_score('{{<a!>},{<a!>},{<a!>},{<ab>}}'))

print(find_score(input))