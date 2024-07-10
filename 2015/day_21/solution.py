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
    with open(filename, 'r') as file: 
        input = []
        type = ''
        for i, line in enumerate(file): 
            line = line.replace('\n', '')
            line = line.split()
            if not len(line):
                continue
            
            if line[-1] == 'Armor':
                type = line[0][:-1]
                continue 
            
            item = {}
            item['armor'] = int(line[-1])
            item['damage'] = int(line[-2])
            item['cost'] = int(line[-3])
            item['type'] = type
            input.append(item)

        input = sorted(input, key=lambda x: x['cost'])
        return input 

input = get_input()
# for x in input:
#     cx)

def get_ring_combinations():
    ring_combinations = []
    rings = []
    for x in input:
        if x['type'] == 'Rings':
            rings.append(x)

    for i, x in enumerate(rings):
        ring_combinations.append(x)
        for j in range(i + 1, len(rings)):
            y = rings[j]
            combo = {}
            combo['cost'] = y['cost'] + x['cost']
            combo['armor'] = y['armor'] + x['armor']
            combo['damage'] = y['damage'] + x['damage']
            ring_combinations.append(combo)
    return sorted(ring_combinations, key= lambda x: x['cost'])

def get_armor_ring_combos():
    ring_combos = get_ring_combinations()
    armors = [x for x in input if x['type'] == 'Armor']
    armor_ring_combos = []
    for a in armors:
        armor_ring_combos.append(a)
        for r in ring_combos:
            combo = {}
            combo['cost'] = r['cost'] + a['cost']
            combo['armor'] = r['armor'] + a['armor']
            combo['damage'] = r['damage'] + a['damage']
            armor_ring_combos.append(combo)
    
    return sorted(armor_ring_combos, key= lambda x: x['cost'])

cost = 0
def add_item(player, item):
    global cost
    player['armor'] += item['armor']
    player['damage'] += item['damage']
    cost += item['cost']

def remove_item(player, item):
    global cost
    player['armor'] -= item['armor']
    player['damage'] -= item['damage']
    cost -= item['cost']

def solve(input):
    global cost
    weapons = [x for x in input if x['type'] == 'Weapons']
    armor_ring_combos = get_armor_ring_combos()
    
    player = {
        'hp': 100,
        'damage': 0,
        'armor': 0,
    }

    boss = {
        'hp': 109,
        'damage': 8,
        'armor': 2
    }

    def wins_fight(player, boss):
        while player['hp'] > 0 and boss['hp'] > 0:
            boss['hp'] -= max(player['damage'] - boss['armor'], 1)
            if boss['hp'] > 0:
                player['hp'] -= max(boss['damage'] - player['armor'], 1)
        wins = player['hp'] > 0
        player['hp'] = 100
        boss['hp'] = 109
        return wins

    min_cost = float('inf')
    
    for weapon in weapons:
        cost = 0
        add_item(player, weapon)
        if wins_fight(player, boss):
            min_cost = min(min_cost, cost)
            remove_item(player, weapon)
            continue
        
        for x in armor_ring_combos:
            add_item(player, x)
            if wins_fight(player, boss):
                min_cost = min(min_cost, cost)
                remove_item(player, x)
                break
            remove_item(player, x)
        
        remove_item(player, weapon)
    return min_cost

# solution = solve(input)
# print(solution)

# Part 2

def solve_part_2(input):
    global cost
    weapons = [x for x in input if x['type'] == 'Weapons']
    armor_ring_combos = get_armor_ring_combos()

    player = {
        'hp': 100,
        'damage': 0,
        'armor': 0,
    }

    boss = {
        'hp': 109,
        'damage': 8,
        'armor': 2
    }

    def wins_fight(player, boss):
        while player['hp'] > 0 and boss['hp'] > 0:
            boss['hp'] -= max(player['damage'] - boss['armor'], 1)
            if boss['hp'] > 0:
                player['hp'] -= max(boss['damage'] - player['armor'], 1)
        wins = player['hp'] > 0
        player['hp'] = 100
        boss['hp'] = 109
        return wins

    max_cost = 0

    for weapon in weapons:
        cost = 0
        add_item(player, weapon)
        if not wins_fight(player, boss):
            max_cost = max(max_cost, cost)

        for armor_ring_combo in armor_ring_combos:
            add_item(player, armor_ring_combo)
            print(cost)
            if not wins_fight(player, boss):
                max_cost = max(max_cost, cost)

            remove_item(player, armor_ring_combo)

        remove_item(player, weapon)
    return max_cost

part_2 = solve_part_2(input)
print(part_2)
# 171 - too low