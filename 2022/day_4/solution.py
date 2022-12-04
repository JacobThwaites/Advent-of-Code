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
            a,b = line.split(',')
            ax = a.split('-')
            bx= b.split('-')
            for i, v in enumerate(ax):
                ax[i] = int(ax[i])
                bx[i] = int(bx[i])
            
            c = [ax, bx]
            input.append(c)

        return input 

input = get_input()
# print(input)

# Part 1
# p = 0

# for x in input:
#     a = x[0]
#     b = x[1]

#     if a[0] >= b[0] and a[1] <= b[1]:
#         p += 1
#     elif b[0] >= a[0] and b[1] <= a[1]:
#         p+=1

# print(p)


# Part 2

p = 0

for x in input:
    a = x[0]
    b = x[1]

    if (a[0] >= b[0] and a[0] <= b[1]) or (a[1] >= b[0] and a[1] <= b[1]):
        p += 1
    elif (b[0] >= a[0] and b[0] <= a[1]) or (b[1] >= a[0] and b[1] <= a[1]):
        p += 1

print(p)