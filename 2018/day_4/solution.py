import sys
import math
import bisect
import re
import hashlib
from math import gcd,floor,sqrt,log, prod
from collections import defaultdict as dd, deque
from bisect import bisect_left as bl, bisect_right as br
from datetime import datetime

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
            line = line.replace('#', '')
            date, info = line.split('] ')
            date = datetime.strptime(date, "%Y-%m-%d %H:%M")
            info = info.split(' ')

            if info[0] == 'Guard':
                info[1] = int(info[1])

            event = {'time': date, 'info': info}
            input.append(event)

        input.sort(key=lambda x: x['time'])
        return input

input = get_input()
# [print(row) for row in input]

guards = []
guard = {'id': None, 'events': []}

for row in input:
    if row['info'][0] == 'Guard':
        if guard['id']:
            guards.append(guard)
        guard['id'] = row['info'][1]
        guard['events'] = []
    elif row['info'][0] == 'falls':
        guard['events'].append(('sleep', row['time']))
    elif row['info'][0] == 'wakes':
        guard['events'].append(('wake', row['time']))

guards.append(guard)
max_time_asleep = 0

for g in guards:
    time_asleep = 0
    sleep_start = None
    for i, e in enumerate(g['events']):
        if e[0] == 'sleep':
            sleep_start = e[1]
        elif e[0] == 'wake' and sleep_start:
            time_asleep += e[1] - sleep_start
    max_time_asleep = max(time_asleep, max_time_asleep)

print(max_time_asleep)