filestream = open('data.txt', 'r') 
data = filestream.readlines()

coordinates = []
instructions = []

for line in data:
    line = line.replace('\n', '')
    if line[0:4] == 'fold':
        instructions.append(line)
    elif line != '':
        coordinates.append(line)

# format coordinates
for i in range(len(coordinates)):
    coordinates[i] = coordinates[i].split(',')
    for j in range(len(coordinates[i])):
        coordinates[i][j] = int(coordinates[i][j])

# format instructions 
for i in range(len(instructions)):
    instructions[i] = instructions[i].replace('fold along ', '')
    instructions[i] = instructions[i].split('=')
    instructions[i][1] = int(instructions[i][1])

def fold(coordinate, instructions):
    axis = instructions[0]
    line = instructions[1]
    index = 0 if axis == 'x' else 1

    if coordinate[index] <= line:
        return coordinate
    
    coordinate[index] = line - (coordinate[index] - line)
    return coordinate

def remove_coordinates_x(coordinates, fold):
    k = len(coordinates) - 1
    while k >= 0:
        if coordinates[k][0] < 0:
            del coordinates[k]
        k -= 1
    return coordinates

def remove_coordinates_y(coordinates, fold):
    k = len(coordinates[0]) - 1
    while k >= 0:
        if coordinates[k][1] < 0:
            del coordinates[k]
        k -= 1
    return coordinates

def remove_lines_outside_fold(coordinates, instruction):
    if instruction[0] == 'x':
        return remove_coordinates_x(coordinates, instruction)
    else:
        return remove_coordinates_y(coordinates, instruction)

def fold_lines(coordinates, instructions):
    for instruction in instructions:
        for j in range(len(coordinates)):
            coordinates[j] = fold(coordinates[j], instruction)
    remove_lines_outside_fold(coordinates, instruction)

fold_lines(coordinates, instructions)

max_x = 0
max_y = 0
unique = set()
for c in coordinates:
    unique.add((c[0], c[1]))
    max_x = max(max_x, c[0])
    max_y = max(max_y, c[1])

# Printing the grid for visualization
for y in range(max_y + 1): 
    print(''.join(['#' if (x, y) in unique else '.' for x in range(max_x + 1)]))

