import statistics
import math
from triangle import TriangleNumberCalculator


filestream = open('data.txt', 'r') 
data = filestream.read()
crabs = data.split(',')
max_crab = 0

for i in range(len(crabs)):
    crabs[i] = int(crabs[i])
    max_crab = max(max_crab, crabs[i])

median = statistics.median(crabs)

median_distance = 0
for c in crabs:
    median_distance += abs(median - c)

triangle_number_calculator = TriangleNumberCalculator()
triangle_number_calculator.calculate_first_n(max_crab)

min_distance = math.inf
for i in range(1, max_crab):
    total_distance = 0
    for c in crabs:
        distance = abs(c - i)
        triangle_distance = triangle_number_calculator.calculate(distance)
        total_distance += triangle_distance
    min_distance = min(min_distance, total_distance)

print(min_distance)