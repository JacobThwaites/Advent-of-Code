import sys
import math
import bisect
import re
import hashlib
from math import gcd,floor,sqrt,log, prod
from collections import defaultdict as dd, deque
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
            line = line.split()
            start = line[1]
            end = line[-3]
            input.append([start, end])

        return input

input = get_input()
# [print(row) for row in input]

steps = {}
for start, end in input:
    if start not in steps:
        steps[start] = []
    if end in steps:
        steps[end].append(start)
    else:
        steps[end] = [start]


def find_next_step(steps, completed):
    available = []

    for k, v in steps.items():
        if not v and k not in completed:
            available.append(k)

    available.sort()
    return available[0]

next = find_next_step(steps, {})

def solve(steps):
    completed = {}
    output = ''

    while len(completed) < len(steps):
        next = find_next_step(steps, completed)
        output += next
        completed[next] = True

        for requirements in steps.values():
            if next in requirements:
                requirements.remove(next)

    return output

# ans = solve(steps)
# print(ans)


# Part 2
def to_num(char):
    return ord(char) - 64

steps = {}
for start, end in input:
    if start not in steps:
        time_remaining = 60 + to_num(start)
        steps[start] = {'blockers': [], 'time_remaining': time_remaining}
    if end not in steps:
        time_remaining = 60 + to_num(end)
        steps[end] = {'blockers': [], 'time_remaining': time_remaining}

    steps[end]['blockers'].append(start)

def find_available_steps(steps, completed, in_progress):
    available = []

    for k, v in steps.items():
        if not v['blockers'] and k not in completed and k not in in_progress:
            available.append(k)

    available.sort()
    return available


def solve2(steps, num_workers):
    time = 0

    workers = []
    for _ in range(num_workers):
        workers.append(None)

    completed = {}
    queue = []
    workers[0] = find_available_steps(steps, completed, workers)[0]

    while len(completed) < len(steps):
        time += 1

        queue = find_available_steps(steps, completed, workers)
        for i, worker in enumerate(workers):
            if not worker and queue:
                workers[i] = queue.pop(0)

        for i, worker in enumerate(workers):
            if worker:
                steps[worker]['time_remaining'] -= 1

                if steps[worker]['time_remaining'] < 1:
                    completed[worker] = True

                    for step in steps.values():
                        if worker in step['blockers']:
                            step['blockers'].remove(worker)
                    workers[i] = None



    return time

ans = solve2(steps, 5)
print(ans)