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

# print(max_distance)

# Part 2
tracker = {}
leaderboard = {}
for name, speed, travel_time, rest_time in input:
    tracker[name] = {
        'speed': speed, 
        'travel_time': travel_time, 
        'rest_time': rest_time,
        'countdown': travel_time,
        'is_resting': False,
        'distance_travelled': 0
    }
    leaderboard[name] = 0

for x in range(total_time):
    leaders = []
    curr_lead_score = 0
    for name, reindeer in tracker.items():
        if not reindeer['is_resting']:
            reindeer['distance_travelled'] += reindeer['speed']
        
        if reindeer['distance_travelled'] == curr_lead_score:
            leaders.append(name)

        elif reindeer['distance_travelled'] > curr_lead_score:
            curr_lead_score = reindeer['distance_travelled']
            leaders = [name]
        
        reindeer['countdown'] -= 1
        if reindeer['countdown'] == 0:
            reindeer['countdown'] = reindeer['travel_time'] if reindeer['is_resting'] else reindeer['rest_time']
            reindeer['is_resting'] = not reindeer['is_resting']

    for leader in leaders:
        leaderboard[leader] += 1
    


highest_score = max(leaderboard.values())
print(highest_score)