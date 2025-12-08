import sys
import math
import bisect
import re
import hashlib
from math import gcd,floor,sqrt,log, prod
from collections import defaultdict as dd, deque
from bisect import bisect_left as bl, bisect_right as br
from typing import List, Dict

sys.setrecursionlimit(100000000)

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

mod=1000000007


def get_input():
    filename = './input.txt'
    filename ='./test.txt'
    with open(filename, 'r') as file:
        input = []
        for line in file:
            line = line.split(',')
            line = tuple(int(x) for x in line)
            input.append(line)

        return input

input = get_input()

def calc_distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

distances = {}

for x in range(len(input)):
    for y in range(x+1, len(input)):
        d = calc_distance(input[x], input[y])
        distances[d] = [input[x], input[y]]


circuits = []

def exists(a, circuits):
    for c in circuits:
        if a in c:
            return True

    return False

def both_exist(a, b, circuits):
    return exists(a, circuits) and exists(b, circuits)

def find_circuit_index(key, circuits):
    for i, c in enumerate(circuits):
        if key in c:
            return i

    return -1

def same_circuit(a, b, circuits):
    a_index = find_circuit_index(a, circuits)
    b_index = find_circuit_index(b, circuits)

    return a_index == b_index and a_index != -1

def merge_circuits(a, b, circuits: List[Dict]):
    a_index = find_circuit_index(a, circuits)
    b_index = find_circuit_index(b, circuits)

    for coordinate, connections in circuits[b_index].items():
        circuits[a_index][coordinate] = connections

    circuits[a_index][a].append(b)
    circuits[a_index][b].append(a)

    circuits.pop(b_index)

test_circuits = [{"a": ["b"]}, {"c": ["d"]}]
merge_circuits('a', 'c', test_circuits)
assert len(test_circuits) == 1

connections = 0
MAX_CONNECTIONS = 1000

for d in sorted(list(distances.keys())):
    if connections == MAX_CONNECTIONS:
        break

    connections +=1

    a, b = distances[d]

    if both_exist(a, b, circuits):
        if same_circuit(a, b, circuits):
            continue

        merge_circuits(a, b, circuits)

    elif exists(a, circuits):
        for c in circuits:
            if a in c:
                c[a].append(b)
                c[b] = [a]
                break
    elif exists(b, circuits):
        for c in circuits:
            if b in c:
                c[b].append(a)
                c[a] = [b]
                break
    else:
        circuit = {}
        circuit[a] = [b]
        circuit[b] = [a]
        circuits.append(circuit)

circuits.sort(key=lambda c : len(c.values()), reverse=True)

print(prod([len(c) for c in circuits[:3]]))

# Part 2

def solve():
    circuits = []

    last_connection = None
    for d in sorted(list(distances.keys())):
        if len(circuits) == 1 and len(circuits[0]) == len(input):
            break

        a, b = distances[d]

        last_connection = [a, b]

        if both_exist(a, b, circuits):
            if same_circuit(a, b, circuits):
                continue

            merge_circuits(a, b, circuits)

        elif exists(a, circuits):
            for c in circuits:
                if a in c:
                    c[a].append(b)
                    c[b] = [a]
                    break
        elif exists(b, circuits):
            for c in circuits:
                if b in c:
                    c[b].append(a)
                    c[a] = [b]
                    break
        else:
            circuit = {}
            circuit[a] = [b]
            circuit[b] = [a]
            circuits.append(circuit)

    return last_connection[0][0] * last_connection[1][0]

ans = solve()
print(ans)
