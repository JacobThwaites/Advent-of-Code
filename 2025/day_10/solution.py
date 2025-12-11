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
    filename ='./test.txt'
    with open(filename, 'r') as file:
        input = []
        for line in file:
            line = line.replace('\n', '')
            line = line.replace('(', '')
            line = line.replace(')', '')
            line = line.replace('[', '')
            line = line.replace(']', '')
            line = line.replace(')', '')
            line = line.replace('{', '')
            line = line.replace('}', '')
            line = line.split(' ')

            lights = list(line[0])
            joltage = [int(n) for n in line[-1].split(',')]
            buttons = line[1:-1]
            for i, b in enumerate(buttons):
                buttons[i] = [int(n) for n in b.split(',')]
            input.append((lights, buttons, joltage))

        return input

input = get_input()

def toggle_button(lights, button):
    new_lights = lights.copy()
    for i in button:
        if new_lights[i] == '#':
            new_lights[i] = '.'
        else:
            new_lights[i] = '#'

    return new_lights

test = toggle_button(['.', '.', '#'], [0, 2])
assert test[0] == '#'
assert test[2] == '.'

def finished(lights, target):
    for i, _ in enumerate(lights):
        if lights[i] != target[i]:
            return False

    return True


def solve(target, buttons):
    seen = set()
    lights = ['.'] * len(target)
    queue = deque([(lights, 0)])
    seen.add(''.join(lights))

    while queue:
        lights, presses = queue.popleft()

        if finished(lights, target):
            return presses

        for b in buttons:
            new_lights = toggle_button(lights, b)
            state = ''.join(new_lights)

            if state not in seen:
                seen.add(state)
                queue.append((new_lights, presses + 1))

    return float('inf')


ans = 0

for lights, buttons, joltage in input:
    ans += solve(lights, buttons)

print(ans)

# Part 2

def is_over(config, target):
    for i, _ in enumerate(config):
        if config[i] > target[i]:
            return True

    return False

assert is_over([1,2,3], [1,2,3]) == False
assert is_over([1, 2, 4], [1, 2, 3]) == True

def finished(config, target):
    for i, _ in enumerate(config):
        if config[i] != target[i]:
            return False

    return True


assert finished([1, 2, 3], [1, 2, 3]) == True
assert finished([1, 2, 2], [1, 2, 3]) == False

def toggle_joltage(joltage, button):
    new_joltage = joltage.copy()

    for i in button:
        new_joltage[i] += 1

    return new_joltage

assert toggle_joltage([0, 1, 2], [0,2]) == [1,1,3]


def solve2(target, buttons):
    seen = set()
    joltage = [0] * len(target)

    queue = deque([(joltage, 0)])
    seen.add(tuple(joltage))

    while queue:
        joltage, presses = queue.popleft()

        if finished(joltage, target):
            return presses

        if is_over(joltage, target):
            continue

        for b in buttons:
            new_joltage = toggle_joltage(joltage, b)
            state = tuple(new_joltage)

            if state not in seen:
                seen.add(state)
                queue.append((new_joltage, presses + 1))

    return float('inf')


ans = 0

for _, buttons, joltage in input:
    test = solve2(joltage, buttons)
    print(test)
    ans += solve2(joltage, buttons)

print(ans)