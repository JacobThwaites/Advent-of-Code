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
            id, connections  = line.split(" <-> ")
            id = int(id)
            connections = connections.replace(', ', '')
            connections = [int(c) for c in connections]
            input.append([id, connections])
            
        return input 

input = get_input()

mapping = {}

for id, connections in input:
    if id not in mapping:
        mapping[id] = {'connections': set()}
    for c in connections:
        if c not in mapping:
            mapping[c] = {'connections': set()}
        mapping[id]['connections'].add(c)
        mapping[c]['connections'].add(id)
        
# print(mapping)

visited = {0: True}

queue = [c for c in mapping[0]['connections']]

while len(queue):
    next = queue.pop(0)
    
    if next not in visited:
        visited[next] = True
        
        for c in mapping[next]['connections']:
            if c not in visited:
                queue.append(c)

print(len(visited.keys()))
