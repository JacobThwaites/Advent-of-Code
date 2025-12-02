import sys
import math
import bisect
import re
import hashlib
from math import gcd,floor,sqrt,log, prod
from collections import defaultdict as dd, deque
from bisect import bisect_left as bl, bisect_right as br

sys.setrecursionlimit(100000000)

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

mod=1000000007


input = 'lpvhkcbi'
# input = 'ulqzkmiv'  # test

def is_oob(x, y):
    return x < 0 or y < 0 or x >= 4 or y >= 4

def is_open(letter):
    return letter in 'bcdef'

explored_paths = {}

shortest = float('inf')
path = ""
paths = []

def search(x: int, y: int, path: str):
    if x == 3 and y == 3:
        paths.append(path)
        global shortest
        if len(path) < shortest:
            print(path)
        shortest = min(shortest, len(path))
        return path

    if path in explored_paths:
        return

    if is_oob(x, y):
        return

    hash = hashlib.md5((f'{input}{path}').encode()).hexdigest()[:4]

    if is_open(hash[0]):
        search(x-1, y, path+"U")
    if is_open(hash[1]):
        search(x+1, y, path+"D")
    if is_open(hash[2]):
        search(x, y-1, path+"L")
    if is_open(hash[3]):
        search(x, y+1, path+"R")

search(0,0,"")


mx = 0
p = ''

for path in paths:
    if len(path) > mx:
        mx = len(path)
        p = path

print(len(p))
