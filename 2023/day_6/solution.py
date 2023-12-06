import sys
import math
import bisect
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br

sys.setrecursionlimit(100000000)

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

mod=1000000007


def get_input():
    with open('./input.txt', 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            data = line.split()

            input.append((int(data[1]),int(data[2]),int(data[3]), int(data[4])))

        return input 

input = get_input()
# print(input)

times, distances = input[0], input[1]

total = 1

def is_charge_time_successful(time_charged, time_remaining, distance):
    return time_charged * time_remaining > distance

for i, time in enumerate(times):
    distance = distances[i]
    winning = 0
    for t in range(time):
        if is_charge_time_successful(t, time-t, distance):
            winning += 1
    
    if winning:
        total *= winning

print(total)

# Part 2

def get_input():
    filename = './input.txt'
    # filename ='./test.txt'
    with open(filename, 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            line = line.replace('Time:', '')
            line = line.replace('Distance:', '')
            data = line.split()
            combined = ''.join(data)
            input.append(int(combined))

        return input 

input = get_input()

time, distance = input[0], input[1]

def binary_search_range(time, distance):
    def find_first_index(time, distance):
        start = 1
        end = time + 1
        result = -1

        while start <= end:
            mid = (start + end) // 2

            if is_charge_time_successful(mid, time-mid, distance):
                result = mid
                end = mid - 1
            else:
                start = mid + 1

        return result

    def find_last_index(time, distance):
        start = 1
        end = time + 1
        result = -1

        while start <= end:
            mid = (start + end) // 2

            if is_charge_time_successful(mid, time-mid, distance):
                result = mid
                start = mid + 1
            else:
                end = mid - 1

        return result

    first_index = find_first_index(time, distance)
    last_index = find_last_index(time, distance)

    return first_index, last_index


first, last = binary_search_range(time, distance)
print(last - first + 1)