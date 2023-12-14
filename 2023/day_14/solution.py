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

rotated = [list(row) for row in zip(*input)]

def find_roll_end(row, rock_index):
    end = rock_index
    for i in range(rock_index-1, -1, -1):
        if row[i] in 'O#':
            return end
        end -= 1
    
    return end

for i, row in enumerate(rotated):
    for j in range(0, len(row)):
        if row[j] == 'O':
            roll_end = find_roll_end(row, j)
            if j != roll_end:
                row[roll_end] = 'O'
                row[j] = '.'

total = 0

for row in rotated:
    for i, val in enumerate(row):
        if val == 'O':
            total += len(row) - i

print(total)
