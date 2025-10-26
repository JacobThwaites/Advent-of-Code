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
            line = line.split(' ')
            input.append(line)

        return input

input = get_input()
# [print(row) for row in input]


s = list("abcde")
s = list("abcdefgh")

def rotate_left(l: list, steps: int) -> list:
    offset = steps % len(l)
    return l[offset:] + l[:offset]


assert rotate_left(list('abcde'), 1) == list('bcdea')

def rotate_right(l: list, steps: int) -> list:
    offset = -(steps % len(l))
    return l[offset:] + l[:offset]

assert rotate_right(list('abcde'), 1) == list('eabcd')

def rotate(l: list, steps: int, direction: str) -> list:
    if direction == 'right':
        return rotate_right(l, steps)
    else:
        return rotate_left(l, steps)

def rotate_based_on_letter(l: list, letter: str) -> list:
    index = l.index(letter)

    steps = 1 + index
    if index >= 4:
        steps += 1

    return rotate_right(l, steps)

assert rotate_based_on_letter(list('ecabd'), 'd') == list('decab')

def reverse(l: list, start: int, end: int) -> list:
    left, right = start, end

    while left < right:
        l[left], l[right] = l[right], l[left]

        left += 1
        right -= 1

    return l

assert reverse(list('abcde'), 1, 3) == list('adcbe')

assert reverse(list('edcba'), 0, 4) == list('abcde')

def move(l: list, start: int, end: int) -> list:
    letter = l[start]
    l.pop(start)
    l.insert(end, letter)
    return l

assert move(list('bcdea'), 1, 4) == list('bdeac')

for row in input:
    if row[0] == 'swap':
        if row[1] == 'position':
            x, y = int(row[2]), int(row[-1])
            s[x], s[y] = s[y], s[x]
        elif row[1] == 'letter':
            x = s.index(row[2])
            y = s.index(row[-1])
            s[x], s[y] = s[y], s[x]
    elif row[0] == 'rotate':
        if row[1] == 'based':
            s = rotate_based_on_letter(s, row[-1])
        else:
            steps = int(row[2])
            direction = row[1]
            s = rotate(s, steps, direction)
    elif row[0] == 'reverse':
        start = int(row[2])
        end = int(row[-1])
        s = reverse(s, start, end)
    elif row[0] == 'move':
        start = int(row[2])
        end = int(row[-1])
        s = move(s, start, end)

print("".join(s))


def unscramble_rotate(l: list, steps: int, direction: str) -> list:
    if direction == 'right':
        return rotate_left(l, steps)
    else:
        return rotate_right(l, steps)


def unscramble_rotate_based_on_letter(l: list, letter: str) -> list:
    for i in range(len(l)):
        test = rotate_left(l, i)
        if rotate_based_on_letter(test, letter) == l:
            return test
    raise ValueError("No valid unscramble rotation found.")

def unscramble(s):
    input.reverse()

    for row in input:
        if row[0] == 'swap':
            if row[1] == 'position':
                x, y = int(row[2]), int(row[-1])
                s[x], s[y] = s[y], s[x]
            elif row[1] == 'letter':
                x = s.index(row[2])
                y = s.index(row[-1])
                s[x], s[y] = s[y], s[x]
        elif row[0] == 'rotate':
            if row[1] == 'based':
                s = unscramble_rotate_based_on_letter(s, row[-1])
            else:
                steps = int(row[2])
                direction = row[1]
                s = unscramble_rotate(s, steps, direction)
        elif row[0] == 'reverse':
            start = int(row[2])
            end = int(row[-1])
            s = reverse(s, start, end)
        elif row[0] == 'move':
            start = int(row[-1])
            end = int(row[2])
            s = move(s, start, end)

    return "".join(s)

print(unscramble(list('fbgdceah')))
