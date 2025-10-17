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

target = int(input[0])

calculated = {}


def find_divisors(num):
    if num in calculated:
        return calculated[num]

    divisors = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)

    calculated[num] = divisors
    return divisors


def calculate_house_total(num):
    total = 0

    divisors = find_divisors(num)

    for d in divisors:
        total += 10 * d

    return total

# for num in range(1, 100000000):
#     total = calculate_house_total(num)

#     if total >= target:
#         print(num)
#         break


# Part 2

mx = target // 10
houses = [0] * (target + 1)

for x in range(1, mx + 1):
    total_visits = 0
    for house in range(x, mx + 1, x):
        if total_visits >= 50:
            break

        houses[house] += 11 * x
        total_visits += 1


for i, h in enumerate(houses):
    if h >= target:
        print(i)
        break