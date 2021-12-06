report = open('report.txt', 'r')
lines = report.readLines()

prev = int(lines[0]) + int(lines[1]) + int(lines[2])
total_increases = 0
right = 2

while right < len(lines) - 1:
    right += 1
    new_window = int(lines[right]) + int(lines[right - 1]) + int(lines[right - 2])
    if new_window > prev:
        total_increases += 1
    prev = new_window

print(total_increases)