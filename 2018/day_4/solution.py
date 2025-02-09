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
    filename ='./test.txt'
    with open(filename, 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            line = line.replace('[', '')
            datetime, event = line.split('] ')
            date, time = datetime.split(' ')
            hours, minutes = time.split(':')
            year, month, day = date.split('-')
            
            event = event.replace('#', '')
            input.append([[int(year), int(month), int(day)], [int(hours), int(minutes)], event.split(' ')])

        return input 

input = get_input()
# [print(row) for row in input]

input = sorted(input, key=lambda x: (x[0], x[1], x[2]))
# [print(row) for row in input]

def increment_time(time):
    hours, minutes = time
    minutes += 1
    if minutes > 59:
        if hours >= 23:
            return [hours, minutes]
        minutes = 0
        hours += 1
    
    return [hours, minutes]

def increment_date(date):
    date[-1] += 1
    return date

def datetime_diff(d1, d2):
    pass


guards = {}

asleep = False
guard_id = None
for i, info in enumerate(input):
    date, time, event = info
    

    if event[0] == 'falls':
        asleep = True
    elif event[0] == 'wakes':
        asleep = False
    else:
        guard_id = event[1]
        
    if guard_id not in guards:
        guards[guard_id] = dd(int)
    
    if i < len(input) - 2:    
        next_date, next_time, next_event = input[i+1]
    print(i+1, date, time, event)
    
    reached_next_event = False
    while True:
        if i < len(input) - 2 and time[0] <= next_time[0] and time[1] == next_time[1]:
            print('next event')
            # Reached time of next event
            break
        
        if asleep:
            guards[guard_id][f'{str(time[0])}{str(time[1])}'] += 1
        time = increment_time(time)
        if time[0] == 23 and time[1] > 59:
            print(date, time, event)
            date = increment_date(date)
            time = [0, 0]
    
totals = {}

for id, minutes in guards.items():
    total = 0
    
    for count in minutes.values():
        total += count
    
    totals[id] = total

print(totals)