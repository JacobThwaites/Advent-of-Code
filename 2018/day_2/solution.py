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
            input.append(line)

        return input 

input = get_input()
# [print(row) for row in input]


exactly_two = 0
exactly_three = 0

for row in input:
    contains_two = False 
    contains_three = False
    counts = dd(int)
    for char in row:
        counts[char] += 1
    
    for char, count in counts.items():
        if count == 2:
            contains_two = True
        if count == 3:
            contains_three = True
        
    if contains_two:
        exactly_two += 1
    if contains_three:
        exactly_three += 1

# print(exactly_three * exactly_two)

# Part 2
for x, string in enumerate(input):
    for comparison in input[x+1:]:
        diff = 0
        for x, _ in enumerate(comparison):
            if string[x] != comparison[x]:
                diff += 1
        if diff == 1:
            char = ''
            for x in range(len(string)):
                if string[x] == comparison[x]:
                    char += string[x]
            print(char)