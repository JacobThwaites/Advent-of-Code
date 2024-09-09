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
            line = line.split(' ')
            input.append(line)

        return input 

input = get_input()
# [print(row) for row in input]

total = 0

def row_score(row):
    words = {}
    for word in row:
        if word in words:
            return 0
        words[word] = True
    
    return 1

for row in input:
    total += row_score(row)

# print(total)

# Part 2

def row_score(row):
    words = {}
    for word in row:
        word = sorted(word)
        word = ''.join(word)
        if word in words:
            return 0
        words[word] = True

    return 1


total = 0

for row in input:
    total += row_score(row)

print(total)
