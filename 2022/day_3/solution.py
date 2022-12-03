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

        x = []
        for line in file: 
            line = line.replace('\n', '')
            x.append(line)
            if len(x) > 2:
                input.append(x)
                x = []

        return input 

input = get_input()
# print(input)

sm = 0
for x in input:
    l = {}

    for i in x[0]:
        if i in x[1] and i in x[2]:
            l[i] = 1
    
    for k,v in l.items():
        if k.isupper():
            sm += ord(k) - 38
            break
        else:
            sm += ord(k) - 96
            break
            

print(sm)


# sm = 0

# for x in input:
#     a_letters = {}

#     for a in x[0]:
#         if a not in a_letters:
#             a_letters[a] = 1
    
#     for b in x[1]:
#         if b in a_letters:
#             if b.isupper():
#                 sm += ord(b) - 38
#                 print(b)
#                 print(ord(b) - 38)
#                 break
#             else:
#                 sm += ord(b) - 96
#                 print(b)
#                 print(ord(b) - 96)
#                 break

# print(sm)
