# Get Paths
paths = {}

filestream = open('data.txt', 'r') 
data = filestream.readlines()

for line in data:
    line = line.replace('\n', '')
    line = line.split('-')
    if line[0] not in paths:
        paths[line[0]] = set()

    if line[1] not in paths:
        paths[line[1]] = set()
    
    paths[line[0]].add(line[1])
    paths[line[1]].add(line[0])

del paths['end']
print(paths)

unique_paths = set()

def part1(data, path=['start']):
    final = 0
    for point in data[path[-1]]:
        if point.isupper() or point not in path:
            if point != 'end':
                part1(data, path + [point])
            final += 1
            # if point == 'end':
            #     final += 1
            # else:
            #     part1(data, path + [point])
            # final += 1 if point == 'end' else part1(data, path + [point])
    return final

test = part1(paths)
print(test)