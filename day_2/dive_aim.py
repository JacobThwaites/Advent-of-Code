data = open('directions.txt', 'r')
directions = data.readLines()

horizontal_position = 0
depth = 0
aim = 0

for direction in directions: 
    split_line = direction.split(' ')
    amount = int(split_line[1].strip('\n'))

    if split_line[0] == 'forward':
        horizontal_position += amount
        depth += aim * amount 
    elif split_line[0] == 'down':
        aim += amount 
    else: 
        aim -= amount 

print(horizontal_position)
print(depth)
print(horizontal_position * depth)
