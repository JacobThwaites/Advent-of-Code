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
            if len(line) >= 1:
                input.append(int(line))
            else:
                input.append('')

        input.append('')
        return input 

input = get_input()

mx = 0
ranks = []
curr = 0

for l in input:
    if l == '':
        ranks.append(curr)
        ranks.sort()
        curr = 0
    else:
        curr += l 

ranks.reverse()
# print(ranks)
top = sum(ranks[0:3])
print(top)
# print(mx)