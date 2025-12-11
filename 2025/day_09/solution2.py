import sys
sys.setrecursionlimit(1000000)

# ---------- Input ----------


def get_input():
    filename = './input.txt'
    # filename ='./test.txt'
    with open(filename, 'r') as file:
        input = []
        for line in file:
            line = [int(x) for x in line.split(',')]
            input.append((line[0], line[1]))
        return input


input = get_input()

# ---------- Part 1 ----------
mx = 0
for i, num1 in enumerate(input):
    for j in range(i+1, len(input)):
        num2 = input[j]
        x_distance = abs(num2[0] - num1[0]) + 1
        y_distance = abs(num2[1] - num1[1]) + 1
        mx = max(mx, x_distance * y_distance)
print("Part 1:", mx)

# ---------- Part 2: Weighted Coordinate Compression ----------
# Collect all x and y coordinates
xs = set()
ys = set()
for x, y in input:
    xs.add(x)
    ys.add(y)

# Also include adjacent cells to preserve edges for the outline/fill
for x, y in input:
    xs.add(x + 1)
    xs.add(x - 1)
    ys.add(y + 1)
    ys.add(y - 1)

# Sort and compress
xs = sorted(xs)
ys = sorted(ys)
x_idx = {x: i for i, x in enumerate(xs)}
y_idx = {y: i for i, y in enumerate(ys)}

# Map input to compressed coordinates
compressed_input = [(x_idx[x], y_idx[y]) for x, y in input]

# ---------- Build compressed grid ----------
W, H = len(xs), len(ys)
grid = [['.' for _ in range(W)] for _ in range(H)]

# Order coordinates for outline
coordinates = [compressed_input[0]]
while len(coordinates) < len(compressed_input):
    prev = coordinates[-1]
    next_coord = None
    min_dist = float('inf')
    for c in compressed_input:
        if c in coordinates:
            continue
        if c[0] != prev[0] and c[1] != prev[1]:
            continue
        dist = abs(c[0]-prev[0]) * abs(c[1]-prev[1])
        if dist < min_dist:
            min_dist = dist
            next_coord = c
    coordinates.append(next_coord)
coordinates.append(coordinates[0])

# Draw outline
for i in range(1, len(coordinates)):
    curr = coordinates[i]
    prev = coordinates[i-1]
    grid[curr[1]][curr[0]] = '#'
    grid[prev[1]][prev[0]] = '#'
    pointer = [curr[0], curr[1]]
    while pointer[0] != prev[0] or pointer[1] != prev[1]:
        if pointer[0] < prev[0]:
            pointer[0] += 1
        elif pointer[0] > prev[0]:
            pointer[0] -= 1
        elif pointer[1] < prev[1]:
            pointer[1] += 1
        elif pointer[1] > prev[1]:
            pointer[1] -= 1
        if grid[pointer[1]][pointer[0]] != '#':
            grid[pointer[1]][pointer[0]] = 'X'

# Flood fill


def fill(x, y):
    if x < 0 or y < 0 or x >= W or y >= H:
        return
    if grid[y][x] in '#X':
        return
    grid[y][x] = 'X'
    fill(x+1, y)
    fill(x-1, y)
    fill(x, y+1)
    fill(x, y-1)


fill(coordinates[0][0]+1, coordinates[0][1]+1)

# ---------- Rectangle check ----------


def is_valid_rectangle(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    start_x, end_x = min(x1, x2), max(x1, x2)
    start_y, end_y = min(y1, y2), max(y1, y2)
    for y in range(start_y, end_y+1):
        for x in range(start_x, end_x+1):
            if grid[y][x] not in '#X':
                return False
    return True


# ---------- Find max rectangle ----------
mx = 0
n = len(compressed_input)
for i in range(n):
    c1 = compressed_input[i]
    for j in range(i+1, n):
        c2 = compressed_input[j]
        if c1[0] == c2[0] or c1[1] == c2[1]:
            continue
        if is_valid_rectangle(c1, c2):
            # Weighted area using original coordinates
            width = abs(xs[c2[0]] - xs[c1[0]]) + 1
            height = abs(ys[c2[1]] - ys[c1[1]]) + 1
            mx = max(mx, width * height)

print("Part 2:", mx)
