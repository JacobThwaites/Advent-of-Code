import sys
import math
import bisect
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd, Counter
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
            id, data = line.split(' @ ')
            a, b = data.split(': ')
            x, y = a.split(',')
            width, height = b.split('x')
            input.append([int(x), int(y), int(width), int(height), id])

        return input 

input = get_input()
# [print(row) for row in input]

coordinates = Counter()

for x,y,width,height,id in input:
    for i in range(height):
        for j in range(width):
            curr = (x + j, y + i)
            coordinates[curr] += 1


filtered = {item: count for item, count in coordinates.items() if count >= 2}

print(len(filtered.items()))

for x, y, width, height, id in input:
    unique = True
    for i in range(height):
        for j in range(width):
            curr = (x + j, y + i)
            if coordinates[curr] != 1:
                unique = False 
                break 
    
    if unique:
        print(id)

    
