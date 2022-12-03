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
            input.append(line)

        return input[0]

input = get_input()
print(input)

def v(s):
    pair = False
    sub = False 
    for i, c in enumerate(s):
        if c == 'i' or c == 'o' or c == 's':
            return False 
        if i < len(s) - 2 and s[i+1] == c:
            pair = True
        
        if i > 1 and ord(s[i-2]) == ord(s[i-1]) - 1 and ord(s[i-1]) == ord(s[i]) - 1:
            sub = True 
        
    return pair and sub

s = input
while True: 
    print(s)
    if v(s):
        print(s)
        break

    ords = []
    for c in s:
        ords.append(ord(c))
    
    i = len(ords) - 1
    ords[i] += 1
    while i >= 0:
        if ords[i] > 122:
            ords[i-1] += ords[i] - 122
            ords[i] = 97
            i -= 1
        else:
            i = -1
    
    s = ''
    for c in ords:
        s += chr(c)
