import math

filestream = open('data.txt', 'r') 
data = filestream.readlines()

matrix = []

for line in data:
    line = line.replace('\n', '')
    row = list(line)
    for i in range(len(row)):
        row[i] = int(row[i])
    matrix.append(row)

# print(matrix)

def get_height_difference(x, y):
    max_diff = 0
    coordinate = matrix[x][y]
    if x > 0:
        max_diff = max(max_diff, matrix[x - 1][y])
    
    if x < len(matrix) - 1:
        max_diff = max(max_diff, matrix[x + 1][y])

    if y > 0:
        max_diff = max(max_diff, matrix[x][y - 1])
    
    if x < len(matrix[x]):
        max_diff = max(max_diff, matrix[x][y + 1])

    return max_diff

def is_low_point(x, y):
    height = matrix[x][y]

    if x > 0:
        if height >= matrix[x - 1][y]:
            return False
    
    if x < len(matrix) - 1:
        if height >= matrix[x + 1][y]:
            return False

    if y > 0:
        if height >= matrix[x][y - 1]:
            return False
    
    if y < len(matrix[x]) - 1:
        if height >= matrix[x][y + 1]:
            return False
    
    return True

sum_low_points = 0

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if is_low_point(x, y):
            sum_low_points += 1 + matrix[x][y]

# print(sum_low_points)


# Part 2 

def calculate_max_basins(matrix):
        max_basins = [0,0,0]
        
        def dfs(row, col):
#             return 0 if edge of map reached
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[row]):
                return 0
            
            if matrix[row][col] == 9:
                return 0
            
            matrix[row][col] = 9
            
            return 1 + dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row, col + 1)
        
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] != 9:
                    basin = dfs(x,y)
                    max_basins[0] = max(max_basins[0], basin)
                    max_basins.sort()
        
        return max_basins

max_basins = calculate_max_basins(matrix)
print(max_basins[0] * max_basins[1] * max_basins[2])