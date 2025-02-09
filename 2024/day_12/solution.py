import sys
from collections import defaultdict as dd

sys.setrecursionlimit(100000000)

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

mod=1000000007


def get_input():
    filename = './input.txt'
    filename ='./test.txt'
    filename = './test2.txt'
    with open(filename, 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            input.append(line)

        return input 

input = get_input()
# [print(row) for row in input]

def in_bounds(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x])

def square_perimeter(grid, x, y):
    borders = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    
    perimeter = 4
    
    for (bx, by) in borders:
        if in_bounds(grid, bx, by):
            if grid[bx][by] == grid[x][y]:
                perimeter -= 1
    
    return perimeter


def calculate_areas_and_perimeters(grid):
    visited = {}
    
    def dfs(grid, x, y, visited, region):
        if not in_bounds(grid, x, y):
            return (0, 0)
        
        if grid[x][y] != region:
            return (0, 0)
        
        if (x,y) in visited:
            return (0, 0)
        
        visited[(x, y)] = True
        
        perimeter = square_perimeter(grid, x, y)
        
        up = dfs(grid, x+1, y, visited, region)
        down = dfs(grid, x-1, y, visited, region)
        left = dfs(grid, x, y+1, visited, region)
        right = dfs(grid, x, y-1, visited, region)
        
        area = 1 + up[0] + down[0] + left[0] + right[0]
        perimeter += up[1] + down[1] + left[1] + right[1]
        return (area, perimeter)
    
    total = 0
    
    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            area, perimeter = dfs(grid, x, y, visited, val)
            
            total += area * perimeter
    
    return total
    

x = calculate_areas_and_perimeters(input)
# print(x)

# Part 2 

def is_region(grid, x, y, region):
    return in_bounds(grid, x, y) and grid[x][y] == region

def is_border(grid, x, y, region):
    return (not in_bounds(grid, x, y)) or grid[x][y] != region

def calculate_areas_and_sides(grid):
    visited = {}

    def dfs(grid, x, y, visited, region):
        if not in_bounds(grid, x, y):
            return (0, 0)

        if grid[x][y] != region:
            return (0, 0)

        if (x, y) in visited:
            return (0, 0)

        visited[(x, y)] = True
        
        sides = 0
        sides_list = []

        lx, ly = x, y-1
        
        # bottom left corner
        if is_border(grid, x, y-1, region):
            if 
        
        if is_border(grid, lx, ly, region):
            if (is_region(grid, x - 1, y, region) and (x-1, y) in visited) and not is_region(grid, x, y-1, region):
                pass
            elif is_region(grid, x + 1, y, region) and (x+1, y) in visited and not is_region(grid, x, y+1, region):
                pass
            else:
                sides += 1
        
        rx, ry = x, y+1

        if is_border(grid, rx, ry, region):
            if (is_region(grid, x - 1, y, region) and (x-1, y) in visited) and not is_region(grid, x-1, y+1, region):
                pass
            elif is_region(grid, x + 1, y, region) and (x+1, y) in visited and not is_region(grid, x+1, y+1, region):
                pass
            else:
                sides += 1
                
        ux, uy = x-1, y

        if is_border(grid, ux, uy, region):
            if (is_region(grid, x, y-1, region) and (x, y-1) in visited and not is_region(grid, x-1, y-1, region)):
                pass
            elif (is_region(grid, x, y+1, region) and (x, y+1) in visited):
                pass
            else:
                sides_list.append('up')
                sides += 1
                
        dx, dy = x+1, y

        if is_border(grid, dx, dy, region):
            if (is_region(grid, x, y-1, region) and (x, y-1) in visited):
                pass
            elif (is_region(grid, x, y+1, region) and (x, y+1) in visited):
                pass
            else:
                sides_list.append('down')
                sides += 1

        up = dfs(grid, x+1, y, visited, region)
        down = dfs(grid, x-1, y, visited, region)
        left = dfs(grid, x, y+1, visited, region)
        right = dfs(grid, x, y-1, visited, region)
        area = 1 + up[0] + down[0] + left[0] + right[0]
        sides += up[1] + down[1] + left[1] + right[1]
        
        return (area, sides)


    total = 0

    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            if (x, y) not in visited:
                area, sides = dfs(grid, x, y, visited, val)
                print(f'area, sides: {area, sides}')
                total += area * sides

    return total


x = calculate_areas_and_sides(input)
print(x)