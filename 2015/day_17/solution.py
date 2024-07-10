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
            input.append(int(line))

        return sorted(input)

input = get_input()
# print(input)

def generate_subsets(lst):
    def backtrack(start, path):
        subsets.append(path)
        for i in range(start, len(lst)):
            backtrack(i + 1, path + [lst[i]])

    subsets = []
    backtrack(0, [])
    return subsets
        
subsets = generate_subsets(input)
print(len(subsets))
total = 0 
target = 150
# target = 25
valid_combinations = []
for x in subsets:
    if sum(x) == target:
        total += 1
        valid_combinations.append(x)
        
# print(total)

mn = float('inf')
for x in valid_combinations:
    mn = min(mn, len(x))

total_ways = 0

for x in valid_combinations:
    if len(x) == mn:
        total_ways += 1

print(total_ways)