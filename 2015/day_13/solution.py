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
            line = line.replace('.', '')
            line = line.split(' ')
            info = [line[0], line[2], int(line[3]), line[-1]]
            input.append(info)

        return input 

input = get_input()

pairings = dd(dd)

for name, rating, total, next in input:
    pairings[name][next] = total if rating == 'gain' else -total

max_happiness = float('-inf')

def calculate_pairings(person, happiness_level, seated):
    global max_happiness
    if len(seated) == len(pairings):
        end_happiness = happiness_level + pairings[person][seated[0]] + pairings[seated[0]][person]
        max_happiness = max(max_happiness, end_happiness)
        return 
    
    for p in pairings[person]:
        if p not in seated:
            seated.append(p)
            calculate_pairings(p, happiness_level + pairings[person][p] + pairings[p][person], seated)
            seated.pop()

# for person in pairings:
#     calculate_pairings(person, 0, [person])

# print(max_happiness)

# Part 2
pairings['me'] = {}
for person in pairings:
    pairings['me'][person] = 0
    pairings[person]['me'] = 0

for person in pairings:
    calculate_pairings(person, 0, [person])

print(max_happiness)