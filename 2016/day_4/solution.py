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
            line = line.split('-')
            end = line[-1].split('[')
            x = line[:-1]
            x.append(end[0])
            x.append(end[1][:-1])
            input.append(x)

        return input 

input = get_input()

def is_valid(counts, checksum):
    # return True
    for i, char in enumerate(checksum):
        if counts[i][0] != char:
            return False 
    
    return True
 
sector_id_sum = 0
valid = []

for code in input:
    counts = dd(int)
    
    for word in code[:-2]:
        for letter in word:
            counts[letter] += 1

    counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    
    if is_valid(counts, code[-1]):
        valid.append(code)
        sector_id_sum += int(code[-2])

# print(sector_id_sum)

# Part 2
for code in valid:
    words = []
    for word in code[:-2]:
        new = ''
        for letter in word:
            num = ((ord(letter) - 96) + int(code[-2])) % 26
            char = chr(num + 96)
            new = new + char

        words.append(new)
    
    for word in words:
        if word == 'northpole':
            print(code[-2])
    
    # print(words)
