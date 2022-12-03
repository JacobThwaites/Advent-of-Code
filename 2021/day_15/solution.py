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
            l = []
            for c in line:
                l.append(int(c))

            input.append(l)

        return input 

input = get_input()
# print(input)

def is_out_of_bounds(matrix, coordinates):
    return coordinates[0] < 0 or coordinates[0] >= len(matrix) or coordinates[1] < 0 or coordinates[1] >= len(matrix)

def solve(matrix):
    visited = {}
    queue = []
    min_length = float('inf')
    
    def bfs(start, target, curr_length):
        visited[start] = True
        queue.append(start)

        while queue:
            s = queue.pop(0)

            if is_out_of_bounds(matrix, s) or s in visited:
                continue

            if s == target: 
                min_length = min(min_length, curr_length)
                continue
            else:
                up = (s[0] - 1, s[1])
                down = (s[0] + 1, s[1])
                left = (s[0], s[1] - 1)
                right = (s[0], s[1] + 1)
                queue.append(up)
                queue.append(down)
                queue.append(left)
                queue.append(right)

    bfs((0,0), (len(matrix) - 1, len(matrix[0]) - 1), 0)    


