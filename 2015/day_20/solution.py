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
# print(input)

target = int(input[0])
print(target)

def total_divisible(n):
    total = 0
    mx = floor(n / 2) + 1
    
    for x in range(1, mx):
        if n % x == 0:
            total += (x*10)
    
    total += n*10
    return total

def largest_divisor(target):
    for i in range(target // 2, 0, -1):
        if target % i == 0:
            return i
    return 1

def find_target(target):
    divisible = {}
    for x in range(1, target):
        mx = largest_divisor(x)
        if mx in divisible:
            # print(x)
            divisible[x] = divisible[mx] + (x * 10)
        else:
            total = x * 10
            for i in range(1, x // 2):
                total += i * 10
            divisible[x] = total
        
        if divisible[x] >= target:
            return x
    # print(divisible)     

solution = find_target(target)
print(solution)