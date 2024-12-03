import sys
import math
import bisect
from math import gcd,floor,sqrt,log, prod
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
import re

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
    
def calc(string):
    string = string.replace('mul(', '')
    string = string.replace(')', '')
    a,b = string.split(',')
    return (int(a) * int(b))

total = 0
pattern = r"mul\(\d+,\d+\)"

matches = []

for row in input:
    matches += re.findall(pattern, row)

for m in matches:
    total += calc(m)

# Part 2
pattern = r"(mul\(\d+,\d+\))|(do\(\))|(don\'t\(\))"
matches = []

for row in input:
    matches += re.findall(pattern, row)

def get_str(m):
    for s in m:
        if len(s) > 0:
            return s

total = 0
do = True

for m in matches:
    s = get_str(m)
    
    if s == "do()":
        do = True
    elif s == "don't()":
        do = False
    elif do:
        total += calc(s) 

print(total)