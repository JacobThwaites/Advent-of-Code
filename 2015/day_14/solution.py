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
    filename = './input.txt'
    # filename ='./test.txt'
    with open(filename, 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            line = line.split(' ')

            info = [line[0], int(line[3]), int(line[6]), int(line[13])]
            input.append(info)

        return input 

input = get_input()


def get_reindeer_distance(speed, travel_time, rest_time, total_time):
    distance_travelled = 0
    time_passed = 0

    while time_passed < total_time:
        time_remaining = total_time - time_passed
        if time_remaining < travel_time:
            distance_travelled += speed * time_remaining
            break
        
        distance_travelled += speed * travel_time 
        time_passed += travel_time
        time_passed += rest_time

    return distance_travelled

max_distance = 0 
total_time = 2503

for name, speed, travel_time, rest_time in input:
    distance = get_reindeer_distance(speed, travel_time, rest_time, total_time)
    max_distance = max(max_distance, distance)

print(max_distance)