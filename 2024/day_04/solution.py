import sys
import math
import bisect
import re
from math import gcd,floor,sqrt,log, prod
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
    
def get_words(grid, x, y):
    coordinates = [
        [[x, y], [x+1, y], [x+2, y], [x+3, y]],
        [[x, y], [x-1, y], [x-2, y], [x-3, y]],
        [[x, y], [x, y+1], [x, y+2], [x, y+3]],
        [[x, y], [x, y-1], [x, y-2], [x, y-3]],
        [[x, y], [x-1, y-1], [x-2, y-2], [x-3, y-3]],
        [[x, y], [x-1, y+1], [x-2, y+2], [x-3, y+3]],
        [[x, y], [x+1, y+1], [x+2, y+2], [x+3, y+3]],
        [[x, y], [x+1, y-1], [x+2, y-2], [x+3, y-3]]
    ]
    
    words = []
    
    for c in coordinates:
        try:
            s = ""
            for x, y in c:
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
                    raise Exception('out of bounds')
                s += grid[x][y]
            words.append(s)
        except:
            pass
    
    return words

total = 0
for x, row in enumerate(input):
    for y, _ in enumerate(input[x]):
        words = get_words(input, x, y)
        for word in words:
            if word == 'XMAS':
                total += 1

print(total)


# Part 2

def get_words(grid, x, y):
    coordinates = [
        [[x, y], [x-1, y-1], [x-2, y-2]],
        [[x, y], [x-1, y+1], [x-2, y+2]],
        [[x, y], [x+1, y+1], [x+2, y+2]],
        [[x, y], [x+1, y-1], [x+2, y-2]]
    ]

    words = []
    centres = []

    for c in coordinates:
        try:
            s = ""
            for x, y in c:
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
                    raise Exception('out of bounds')
                s += grid[x][y]
            words.append(s)
            centres.append(tuple(c[1]))
        except:
            pass

    return [words, centres]

mas_centres = dd(int)

for x, row in enumerate(input):
    for y, _ in enumerate(input[x]):
        words, centres = get_words(input, x, y)
        for i, word in enumerate(words):
            if word == 'MAS':
                mas_centres[centres[i]] += 1

total = sum([1 for centre in mas_centres.values() if centre > 1])
print(total)