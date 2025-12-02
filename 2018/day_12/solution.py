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
            input.append(line)

        initial_state = input[0]
        notes = {}
        for line in input[2:]:
            line = line.split()
            notes[line[0]] = True if line[2] == '#' else False
        return [initial_state, notes]


state, notes = get_input()


def is_plant_next_turn(state, index, notes):
    if index == 0:
        sub_state = '..' + state[:3]
    elif index == 1:
        sub_state = '.' + state[:4]
    elif index == len(state) - 1:
        sub_state = state[-3:] + '..'
    elif index == len(state) - 2:
        sub_state = state[-4:] + '.'
    else:
        sub_state = state[index-2:index+3]

    if sub_state in notes:
        return notes[sub_state]
    return False


test_notes = {'..#..': True}
assert is_plant_next_turn('#..#..#', 3, test_notes) == True
assert is_plant_next_turn('#.....#', 3, test_notes) == False
assert is_plant_next_turn('#..', 0, test_notes) == True
assert is_plant_next_turn('..#', 2, test_notes) == True
assert is_plant_next_turn('..#.', 2, test_notes) == True


def get_prefixes(state, notes) -> str:
    prefixes = ''
    if '...' + state[:2] in notes:
        prefixes += '#'

    if '....' + state[0] in notes:
        prefixes += '#'

    return prefixes

test_notes = {'...##': True}
assert get_prefixes('##', test_notes) == '#'
assert get_prefixes('.#', test_notes) == ''

def get_suffixes(state, notes) -> str:
    suffixes = ''

    if state[-2:] + '...' in notes:
        suffixes += '#'

    if state[-1] + '....' in notes:
        suffixes += '#'

    return suffixes

test_notes = {'##...': True}
assert get_suffixes('...##', test_notes) == '#'
assert get_suffixes('....#', test_notes) == ''

def next_state(state, notes):
    next = ''

    for i, _ in enumerate(state):
        if is_plant_next_turn(state, i, notes):
            next += '#'
        else:
            next += '.'

    next = get_prefixes(state, notes) + next
    next += get_suffixes(state, notes)
    return next


def next_state(state, notes):
    state = "...." + state + "...."
    next_state = ""
    for i in range(2, len(state) - 2):
        window = state[i-2:i+3]
        next_state += '#' if notes.get(window, False) else '.'
    return next_state.strip('.')

assert next_state('#..#.#..##......###...###', notes) == '#...#....#.....#..#..#..#'
assert next_state('#...#....#.....#..#..#..#',notes) ==  '##..##...##....#..#..#..##'

def count_pots(state):
    total = 0

    for i, char in enumerate(state):
        if char == '#':
            total += i

    return total


total = count_pots(state)
for _ in range(20):
    state = next_state(state, notes)
    print(count_pots(state))

print(state)
# print(total)