filestream = open('data.txt', 'r') 
data = filestream.readlines()

matrix = []
matrix_size = 0

for line in data:
    line = line.replace('\n', '')
    row = list(line)
    for i in range(len(row)):
        row[i] = int(row[i])
        matrix_size += 1
    matrix.append(row)


total_flashes = 0
visited = set()

def step(x, y, have_flashed):
    global total_flashes

    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[x]):
        return 

    if (x,y) in have_flashed:
        return

    matrix[x][y] += 1
    if matrix[x][y] > 9:
        # flash
        total_flashes += 1
        matrix[x][y] = 0
        have_flashed.add((x,y))

        step(x + 1, y, have_flashed)
        step(x - 1, y, have_flashed)
        step(x + 1, y + 1, have_flashed)
        step(x + 1, y - 1, have_flashed)
        step(x - 1, y + 1, have_flashed)
        step(x - 1, y - 1, have_flashed)
        step(x, y + 1, have_flashed)
        step(x, y - 1, have_flashed)

 
all_flashes = []
num_steps = 100
for i in range(1000):
    have_flashed = set()
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            step(x, y, have_flashed)
            if len(have_flashed) == 100:
                all_flashes.append(i + 1)

print('total flashes: ')
print(total_flashes)
print('')
all_flashes.sort()
print(all_flashes[0])