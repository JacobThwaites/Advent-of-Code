import random
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
            input.append(line)

        return input

input = get_input()

s = input[-1]
unformatted_conversions = input[:-2]
conversions = []
for c in unformatted_conversions:
    c = c.split(' => ')
    conversions.append(c)

def has_prefix(string, prefix):
    if len(string) < len(prefix):
        return False

    for i, char in enumerate(prefix):
        if char != string[i]:
            return False

    return True

def find_indexes_of_substring(string, substring):
    indexes = []
    for i, _ in enumerate(string):
        if has_prefix(string[i:], substring):
            indexes.append(i)

    return indexes

molecules = {}

for (input, output) in conversions:
    indexes = find_indexes_of_substring(s, input)
    for i in indexes:
        new = s[0:i] + output + s[i+len(input):]
        molecules[new] = True

print(len(molecules.keys()))


target = s
steps = 0

# shuffle to avoid infinite loops
reverse_conversions = [(o, i) for i, o in conversions]

while target != 'e':
    replaced = False
    random.shuffle(reverse_conversions)
    for o, i in reverse_conversions:
        if o in target:
            target = target.replace(o, i, 1)
            steps += 1
            replaced = True
            break
    if not replaced:
        target = s
        steps = 0

print(steps)
