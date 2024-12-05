import sys
import math
import bisect
import re
from math import gcd,floor,sqrt,log, prod
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
        is_rule = True
        p1_rules = dd(set)
        p2_rules = dd(set)
        updates = []
        input = []
        for line in file: 
            line = line.replace('\n', '')
            
            if len(line) == 0:
                is_rule = False
                continue
            
            if is_rule:
                a,b = line.split('|')
                p1_rules[(int(b))].add(int(a))
                p2_rules[(int(a))].add(int(b))
            else:
                update = line.split(',')
                updates.append([int(u) for u in update])
        input = [p1_rules, p2_rules, updates]
        return input 

input = get_input()
p1_rules, p2_rules, updates = input

def valid(update, rules):
    invalid = False
    for i, _ in enumerate(update):
        if update[i] not in rules:
            continue
        not_allowed = rules[update[i]]
        if not_allowed in update[:i]:
            invalid = True

    return not invalid


def valid(update, rules):
    invalid = False
    for i, num1 in enumerate(update):
        for j, num2 in enumerate(update):
            if j > i and num2 in rules[num1]:
                invalid = True

    return not invalid
    
    
total = 0

incorrect = []
for update in updates:
    is_valid = valid(update, p1_rules)
    if is_valid:
        mid = len(update) // 2
        total += update[mid]
    else:
        incorrect.append(update)

print(total)

# Part 2

total = 0

for update in incorrect:
    sorted_update = []

    while len(update):
        update_rules = dd(set)
        for num in update:
            if num in p2_rules:
                update_rules[num] = p2_rules[num]

        for i, num in enumerate(update):
            is_valid = True
            for values in update_rules.values():
                for rule in values:
                    if rule == num:
                        is_valid = False
            
            if is_valid:
                sorted_update.append(update.pop(i))
                break

    mid = len(sorted_update) // 2
    total += sorted_update[mid]

print(total)