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
            line = line.split(' ')
            if line[0] == 'toggle':
                s = line[1].split(',')
                e = line[3].split(',')
                for i in range(2):
                    s[i] = int(s[i])
                    e[i] = int(e[i])
                input.append([line[0], s, e])
            else:
                s = line[2].split(',')
                e = line[4].split(',')
                for i in range(2):
                    s[i] = int(s[i])
                    e[i] = int(e[i])
                input.append([line[1], s, e])

        return input 

input = get_input()

m = [[0 for _ in range(0, 1000)] for _ in range(0, 1000)]

for i in input:
    s = i[1]
    e = i[2]
    for x in range(s[0], e[0] + 1):
        for y in range(s[1], e[1] + 1):
            if i[0] == 'toggle':
                m[x][y] += 2
            elif i[0] == 'on':
                m[x][y] += 1
            else:
                m[x][y] = max(m[x][y] - 1, 0)

t = 0
for r in m:
    for v in r:
        t += v

print(t)