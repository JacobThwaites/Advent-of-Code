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
            strings = []
            h = []
            
            curr = ''
            is_h = False 
            i = 0
            while i < len(line):
                if line[i] in '[]':
                    if is_h:
                        h.append(curr)
                    else:
                        strings.append(curr)
                    curr = ''
                    is_h = not is_h
                else:
                    curr += line[i]
                
                i += 1       

            if curr:
                if is_h:
                    h.append(curr)
                else:
                    strings.append(curr)
            input.append({"s": strings, 'h': h})     
        return input 

input = get_input()
# [print(row) for row in input]


def contains_abba(x):
    l, r = 0, 3
    
    while r < len(x):
        if x[l] == x[r]:
            if x[l+1] == x[r-1] and x[l] != x[l+1]:
                return True
        l += 1
        r += 1
    
    return False 

def is_row_valid(row):
    for h in row['h']:
        if contains_abba(h):
            return False 
    
    for s in row['s']:
        if contains_abba(s):
            return True 
    
    return False

total = 0
for row in input:
    if is_row_valid(row):
        total += 1
    
# print(total)
            
# Part 2

def get_abas(x):
    abas = []
    l, r = 0, 2
    
    while r < len(x):
        if x[l] == x[r] and x[l+1] != x[l]:
            abas.append((x[l], x[l+1]))
        
        l += 1
        r += 1
        
    return abas
    
def contains_bab(x, a, b):
    l, r = 0, 2
    
    while r < len(x):
        if x[l] == b and x[r] == b and x[l+1] == a:
            return True 
        l+= 1
        r += 1
    
    return False 

def is_valid(row):
    abas = []
    for s in row['s']:
        x = get_abas(s)
        for aba in x:
            abas.append(aba)

    for h in row['h']:
        for aba in abas:
            if contains_bab(h, aba[0], aba[1]):
                return True 
    
    return False


total = 0

for row in input:
    if is_valid(row):
        total += 1

print(total)