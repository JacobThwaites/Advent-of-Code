from collections import deque
import sys
import math
import bisect
import re
from math import gcd,floor,sqrt,log, prod
from collections import defaultdict as dd, deque
from bisect import bisect_left as bl, bisect_right as br

sys.setrecursionlimit(100000000)

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

mod=1000000007


def get_input():
    filename = './input.txt'
    # filename ='./test.txt'
    filename = './test2.txt'
    with open(filename, 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            input.append(line)

        return input 

input = get_input()
# [print(row) for row in input]

def find_start(grid):
    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            if val == 'S':
                return (x, y)
    
    return (-1, -1)

start = find_start(input)

def in_bounds(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x])

def find_path_score(grid, start):
    def dfs(grid, coordinates, visited, score, direction):
        x, y = coordinates
        
        if not in_bounds(grid, x, y):
            return float('inf')
        
        if grid[x][y] == '#':
            return float('inf')
        
        if grid[x][y] == 'E':
            if score == 10038:
                print(visited.keys())
            return score
        
        if (x, y) in visited:
            return float('inf')
        
        visited[(x, y)] = True
        
        
        up = dfs(grid, (x-1, y), visited.copy(), score+1 if direction == 'up' else score+1001, 'up')
        down = dfs(grid, (x+1, y), visited.copy(), score +
                 1 if direction == 'down' else score + 1001, 'down')
        left = dfs(grid, (x, y-1), visited.copy(), score +
                 1 if direction == 'left' else score + 1001, 'left')
        right = dfs(grid, (x, y+1), visited.copy(), score +
                 1 if direction == 'right' else score + 1001, 'right')
        
        return min(up, down, left, right)

    return dfs(grid, start, {}, 0, 'right')
        
# res = find_path_score(input, start)
# print(res)


def new_function(grid, start, end):
    scores = {}
    
    def dfs(grid, coordinates, score, direction):
        x, y = coordinates
        
        if (x,y, direction) in scores:
            return scores[(x,y, direction)]

        if not in_bounds(grid, x, y):
            return float('inf')

        if grid[x][y] == '#':
            return float('inf')

        if grid[x][y] == 'E':
            return score
        
        up = score + 1 if direction == 'up' else score + 1001 
        if (x-1, y, 'up') in scores:
            up += scores[(x-1, y, 'up')]
        else:
            up += dfs(grid, (x-1, y), score, 'up')

        up = dfs(grid, (x-1, y), visited.copy(), score +
                 1 if direction == 'up' else score+1001, 'up')
        down = dfs(grid, (x+1, y), visited.copy(), score +
                   1 if direction == 'down' else score + 1001, 'down')
        left = dfs(grid, (x, y-1), visited.copy(), score +
                   1 if direction == 'left' else score + 1001, 'left')
        right = dfs(grid, (x, y+1), visited.copy(), score +
                    1 if direction == 'right' else score + 1001, 'right')

        return min(up, down, left, right)
    
    queue = deque([end])
    
    
    sx, sy = start
    # TODO: find possible S directions
    while (sx, sy, 'right') and (sx, sy, 'up') not in scores:
        x,y, direction = queue.popleft()
        
        if (x, y, direction) in scores:
            continue
        
        scores[(x, y, direction)] = dfs(grid, (x, y), {}, 0, direction)
        
        queue.append((x-1, y, 'down'))
        queue.append((x+1, y, 'up'))
        queue.append((x, y-1, 'right'))
        queue.append((x, y+1, 'left'))
            

    return dfs(grid, start, {}, 0, 'right')


def find_end(grid):
    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            if val == 'E':
                return (x, y)

    return (-1, -1)

end = find_end(input)

new_function(input, start, end)