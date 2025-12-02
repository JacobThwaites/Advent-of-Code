import sys
import math
import bisect
import re
from math import gcd, floor, sqrt, log, prod
from collections import defaultdict as dd, deque
from bisect import bisect_left as bl, bisect_right as br
import copy

sys.setrecursionlimit(100000000)


def ceil(x): return int(x) if (x == int(x)) else int(x) + 1
def ceildiv(x, d): return x // d if (x % d == 0) else x // d + 1


mod = 1000000007


def get_input():
    filename = './input.txt'
    # filename = './test.txt'
    with open(filename, 'r') as file:
        input = []
        for line in file:
            line = line.replace('\n', '')
            _, line = line.split('contains a ')
            line = line.replace(' and', '')
            line = line.replace(', a ', ',')
            line = line.replace(' a ', ',')
            line = line.replace('.', '')
            line = line.replace('-compatible', '')
            line = line.split(',')

            input.append(line)

        ids = {}
        inc = 1
        for i, row in enumerate(input):
            vals = []
            for x in row:
                name, type = x.split(' ')
                if name not in ids:
                    ids[name] = inc
                    inc += 1
                id = ids[name]
                vals.append([id, type])
            input[i] = vals
        return input


def is_floor_valid(floor):
    """A floor is valid if no microchip will be fried."""
    gens = {id for id, t in floor if t == 'generator'}
    chips = {id for id, t in floor if t == 'microchip'}

    if not gens:
        return True
    for chip in chips:
        if chip not in gens:
            return False
    return True


def is_invalid(floors):
    for f in floors:
        if not is_floor_valid(f):
            return True
    return False


def is_complete(floors):
    for f in floors[:-1]:
        if len(f) > 0:
            return False
    return True


def to_s(floors, lift):
    """Canonical serialization of the state."""
    s = f"{lift}|"
    for i, floor in enumerate(floors):
        items = sorted([f"{id}{t[0]}" for id, t in floor])
        s += ','.join(items) + '|'
    return s


def get_lift_options(floor_items, lift, floor_count):
    """Return all possible combinations of 1 or 2 items with valid next lift floors."""
    results = []
    n = len(floor_items)

    for i in range(n):
        results.append([[floor_items[i]], lift - 1])
        results.append([[floor_items[i]], lift + 1])
        for j in range(i + 1, n):
            results.append([[floor_items[i], floor_items[j]], lift - 1])
            results.append([[floor_items[i], floor_items[j]], lift + 1])

    valid = [r for r in results if 0 <= r[1] < floor_count]
    return valid


def solve(floors):
    visited = set()
    queue = deque()
    queue.append((copy.deepcopy(floors), 0, 0))  # floors, lift, steps

    while queue:
        floors, lift, steps = queue.popleft()

        s = to_s(floors, lift)
        if s in visited:
            continue
        visited.add(s)

        if is_invalid(floors):
            continue

        if is_complete(floors):
            return steps

        lift_options = get_lift_options(floors[lift], lift, len(floors))
        for items_to_move, new_lift in lift_options:
            new_floors = copy.deepcopy(floors)

            for item in items_to_move:
                new_floors[lift].remove(item)
                new_floors[new_lift].append(item)

            if not is_floor_valid(new_floors[lift]):
                continue
            if not is_floor_valid(new_floors[new_lift]):
                continue

            queue.append((new_floors, new_lift, steps + 1))

    return -1


if __name__ == "__main__":
    input_data = get_input()
    ans = solve(input_data)
    print("Answer:", ans)
