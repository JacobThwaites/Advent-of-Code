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
            line[2] = int(line[2])
            input.append((line[0], line[1], line[2]))

        return input 

input = get_input()
# print(input)


graph = []

for line in input:
    start, end, distance = line
    if start in graph:
        graph[start].append((end, distance))
    else:
        graph[start] = [(end, distance)]

# print(graph)

def solve():
    shortest_distance = float('inf')

    def permute(graph, node, visited, distance_travelled, shortest_distance):
        if len(visited) == len(graph):
            return distance_travelled
        
        for n in graph[node]:
            loc, distance = n
            if loc not in visited and loc in graph: 
                visited.append(loc)
                shortest_distance = min(permute(graph, loc, visited, distance_travelled + distance, shortest_distance), shortest_distance)
                visited.pop()
        
        return float('inf')

    for start in graph: 
        permute(graph, start, [], 0, shortest_distance)

    print(shortest_distance)

solve()