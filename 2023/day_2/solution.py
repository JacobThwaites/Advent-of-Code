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
    with open('./input.txt', 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            info = line.split(': ')
            reveals = info[1].split('; ')
            game_id = info[0].split(' ')[1]

            reveals_list = []

            for reveal in reveals:
                colours = reveal.split(', ')
                reveal_counts = {}
                for c in colours: 
                    s = c.split(' ')
                    reveal_counts[s[1]] = int(s[0])
                reveals_list.append(reveal_counts)

            input.append([int(game_id), reveals_list])

        return input 

input = get_input()

invalid_id_sum = 0

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

for game in input:
    reveals = game[1]
    is_possible = True

    for colours in reveals:
        if 'red' in colours and colours['red'] > MAX_RED:
            is_possible = False
            break
        elif 'blue' in colours and colours['blue'] > MAX_BLUE:  
            is_possible = False
            break
        elif 'green' in colours and colours['green'] > MAX_GREEN:
            is_possible = False
            break

    if is_possible:
        invalid_id_sum += game[0]
# print(invalid_id_sum)


# Part 2

min_sets = 0

for game in input:
    reveals = game[1]

    min_blue = 0
    min_green = 0
    min_red = 0
    for colours in reveals:
        if 'red' in colours:
            min_red = max(min_red, colours['red'])
        if 'blue' in colours:  
            min_blue = max(min_blue, colours['blue'])
        if 'green' in colours:
            min_green = max(min_green, colours['green'])
    
    min_sets += min_red * min_blue * min_green

print(min_sets)