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

seed_numbers = []

def get_input():
    with open('./input.txt', 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            input.append(line)

        return input 

input = get_input()
# print(input)

seeds = input[0]
seeds = seeds.replace('seeds: ', '')
seed_numbers = sorted([int(s) for s in seeds.split(' ')])

def get_categories(input):
    categories = {}

    new_category = True 
    category = ''

    for line in input:
        if new_category:
            categories[line] = []
            category = line
            new_category = False
        elif line == '':
            new_category = True 
            category = ''
        else:
            nums = line.split(' ')
            nums = [int(n) for n in nums]
            categories[category].append(nums)

    return categories

categories = get_categories(input)

def get_mins(nums, data):
    mins = []

    for num in nums: 
        min = num
        for mp in data:
            if mp[1] <= num < mp[1] + mp[2]:
                min = num - mp[1] + mp[0]
        mins.append(min)

    return mins

seed_soil = categories['seed-to-soil map:']
soil_fertilizer = categories['soil-to-fertilizer map:']
fertilizer_water = categories['fertilizer-to-water map:']
water_light = categories['water-to-light map:']
light_temperature = categories['light-to-temperature map:']
temperature_humidity = categories['temperature-to-humidity map:']
humidity_location = categories['humidity-to-location map:']

soil = get_mins(seed_numbers, seed_soil)
fertilizer = get_mins(soil, soil_fertilizer)
water = get_mins(fertilizer, fertilizer_water)
light = get_mins(water, water_light)
temp = get_mins(light, light_temperature)
hum = get_mins(temp, temperature_humidity)
location = get_mins(hum, humidity_location)
print(min(location))


# Part 2
seed_pairs = [seed_numbers[i:i+2] for i in range(0, len(seed_numbers), 2)]
print(seed_pairs)

