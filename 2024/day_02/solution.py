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
            nums = line.split(' ')
            input.append([int(n) for n in nums])

        return input 

input = get_input()
# [print(row) for row in input]

def is_safe(row):
    if row[0] == row[1]:
        return False
    
    increasing = True if row[0] < row[1] else False

    for i, num in enumerate(row):
        if i == 0:
            continue
        
        if increasing:
            if row[i] <= row[i-1] or row[i] > (row[i-1] + 3):
                return False
        
        if not increasing:
            if (row[i] >= row[i-1] or row[i] < (row[i-1] - 3)):
                return False
    
    return True
        

safe = 0
for row in input:
    if is_safe(row):
        safe += 1

# print(safe)
        
# Part 2
def is_increasing(row):
    for i in range(1, len(row)):
        if row[i] <= row[i-1] or row[i] > row[i-1] + 3:
            return False
        
    return True


def is_decreasing(row):
    for i in range(1, len(row)):
        if row[i] >= row[i-1] or row[i] < row[i-1] - 3:
            return False
        
    return True


def is_safe(row):
    if is_increasing(row) or is_decreasing(row):
        return True
    
    for i, _ in enumerate(row):
        new_row = row[:i] + row[i+1:]
        if is_increasing(new_row) or is_decreasing(new_row):
            return True

    return False


safe = 0
for row in input:
    if is_safe(row):
        safe += 1

print(safe)
