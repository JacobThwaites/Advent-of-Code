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
    with open('./input.txt', 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            input.append(line)

        return input 

input = get_input()

# Part 1

digits = []

for s in input: 
    first, last = None, None

    for char in s:
        if char.isdigit():
            if not first:
                first = char
            last = char
    digits.append([first, last])

sm = 0
for d in digits:
    combined = d[0] + d[1]
    sm += int(combined)

print('first answer')
print(sm)

# Part 2

digitsStrings = {
    "one": '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6', 
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

digits = []

for s in input: 
    first, last = None, None

    for i, char in enumerate(s):
        if char.isdigit():
            if not first:
                first = char
            last = char
        elif s[i:i+3] in digitsStrings.keys():
            digit = digitsStrings[s[i:i+3]]
            if not first:
                first = digit
            last = digit
        elif s[i:i+4] in digitsStrings.keys():
            digit = digitsStrings[s[i:i+4]]
            if not first:
                first = digit
            last = digit  
        elif s[i:i+5] in digitsStrings.keys():
            digit = digitsStrings[s[i:i+5]]
            if not first:
                first = digit
            last = digit         
        
    digits.append([first, last])

sm = 0
for d in digits:
    combined = d[0] + d[1]
    sm += int(combined)

print('second answer')
print(sm)