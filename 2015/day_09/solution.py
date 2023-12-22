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
    # filename = './test.txt'
    with open(filename, 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            line = line.split(' ')
            input.append((line[0], line[1], int(line[2])))

        return input 

input = get_input()
# print(input)

graph = dd(dd)
locations = {}

for start, end, distance in input:
    locations[start] = True
    locations[end] = True
    graph[start][end] = distance
    graph[end][start] = distance

min_route = float('inf')
    
def get_paths(location, distance, visited):
    global min_route
    if len(visited) == len(locations):
        min_route = min(distance, min_route)
        return

    nodes = graph[location]

    for node in nodes:
        if node not in visited:
            visited.append(node)
            get_paths(node, distance + graph[location][node], visited)
            visited.pop()

for location in locations:
    get_paths(location, 0, [location])
    
print(min_route)