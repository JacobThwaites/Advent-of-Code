import sys
import math
import bisect
from math import gcd,floor,sqrt,log, prod
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
from itertools import combinations

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

        return input 

input = get_input()
# [print(row) for row in input]

input.sort(reverse=True)

def find_min(packages):
    target_weight = sum(packages) // 4

    for size in range(1, len(packages)):
        valid_groups = [group for group in combinations(
            packages, size) if sum(group) == target_weight]

        if valid_groups:
            min_qe = min(prod(group) for group in valid_groups)
            return min_qe


input = get_input()
result = find_min(input)
print(result)
