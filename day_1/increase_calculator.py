report = open('report.txt', 'r')
lines = report.readLines()

prev = int(lines[0])
total_increases = 0

for i in range(1, len(lines)):
    if int(lines[i]) > prev:
        total_increases += 1
    prev = int(lines[i])

print(total_increases)