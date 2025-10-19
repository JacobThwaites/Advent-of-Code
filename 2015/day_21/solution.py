import sys
import math
import bisect
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br

sys.setrecursionlimit(100000000)


def ceil(x): return int(x) if (x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if (x % d == 0) else x//d+1


mod = 1000000007

def get_input():
    filename = './input.txt'
    with open(filename, 'r') as file:
        items = []
        type_ = ''
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            if parts[-1] == 'Armor' or parts[-1] == 'Weapons' or parts[-1] == 'Rings':
                type_ = parts[0][:-1]
                continue

            item = {
                'type': type_,
                'cost': int(parts[-3]),
                'damage': int(parts[-2]),
                'armor': int(parts[-1])
            }
            items.append(item)

    return items


input_items = get_input()

def get_armor_ring_combos(input_items):
    armors = [x for x in input_items if x['type'] == 'Armor']
    armors.append({'cost': 0, 'damage': 0, 'armor': 0,
                  'type': 'Armor'})

    rings = [x for x in input_items if x['type'] == 'Rings']
    ring_combos = [[]]
    ring_combos += [[r] for r in rings]
    ring_combos += [list(c) for c in combinations(rings, 2)]

    combos = []
    for a in armors:
        for rcombo in ring_combos:
            total = {
                'cost': a['cost'] + sum(r['cost'] for r in rcombo),
                'damage': a['damage'] + sum(r['damage'] for r in rcombo),
                'armor': a['armor'] + sum(r['armor'] for r in rcombo)
            }
            combos.append(total)
    return combos


def does_player_win(player, boss):
    player_turns = -(-boss['hp'] // max(player['damage'] - boss['armor'], 1))
    boss_turns = -(-player['hp'] // max(boss['damage'] - player['armor'], 1))
    return player_turns <= boss_turns


def solve_part_1(input_items):
    weapons = [x for x in input_items if x['type'] == 'Weapons']
    armor_ring_combos = get_armor_ring_combos(input_items)

    boss = {'hp': 109, 'damage': 8, 'armor': 2}
    max_cost = float('inf')

    for w in weapons:
        for ar in armor_ring_combos:
            player = {
                'hp': 100,
                'damage': w['damage'] + ar['damage'],
                'armor': w['armor'] + ar['armor']
            }
            total_cost = w['cost'] + ar['cost']
            if does_player_win(player, boss):
                max_cost = min(max_cost, total_cost)
    return max_cost


def solve_part_2(input_items):
    weapons = [x for x in input_items if x['type'] == 'Weapons']
    armor_ring_combos = get_armor_ring_combos(input_items)

    boss = {'hp': 109, 'damage': 8, 'armor': 2}
    max_cost = 0

    for w in weapons:
        for ar in armor_ring_combos:
            player = {
                'hp': 100,
                'damage': w['damage'] + ar['damage'],
                'armor': w['armor'] + ar['armor']
            }
            total_cost = w['cost'] + ar['cost']
            if not does_player_win(player, boss):
                max_cost = max(max_cost, total_cost)
    return max_cost

part_1 = solve_part_1(input_items)
part_2 = solve_part_2(input_items)

print("Part 1:", part_1)
print("Part 2:", part_2)
