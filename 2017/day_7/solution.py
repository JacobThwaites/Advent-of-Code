# <keep your imports and get_input() and tree construction exactly as before>
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
    # filename ='./test.txt'
    with open(filename, 'r') as file:
        input = []
        for line in file:
            line = line.replace('\n', '')
            line = line.split(' -> ')
            name, weight = line[0].split(' ')
            weight = weight.replace('(', '')
            weight = weight.replace(')', '')
            info = {
                'name': name,
                'weight': int(weight)
            }

            if len(line) == 2:
                line[1] = line[1].replace(',', '')
                leaves = line[1].split(' ')
                info['leaves'] = leaves

            input.append(info)

        return input


input = get_input()

tree = {}

for row in input:
    tree[row['name']] = row
    tree[row['name']]['children'] = {}

nodes_to_delete = []
for name, node in tree.items():
    if 'leaves' in node:
        for leaf_name in node['leaves']:
            leaf_node = tree[leaf_name]
            node['children'][leaf_name] = leaf_node
            nodes_to_delete.append(leaf_name)
        del node['leaves']

for name in nodes_to_delete:
    del tree[name]

root = None
for name in tree.keys():
    root = name
# print(root)

# Part 2


def find_branch_weight(node):
    weight = node['weight']
    for child in node['children'].values():
        weight += find_branch_weight(child)
    node['total_branch_weight'] = weight
    return weight


def find_cause(node):
    for child in node['children'].values():
        res = find_cause(child)
        if res is not None:
            return res

    child_nodes = list(node['children'].values())
    if len(child_nodes) == 0:
        return None

    name_weights = [(n['name'], n['total_branch_weight'], n['weight'])
                    for n in child_nodes]
    weights_only = [w for (_, w, _) in name_weights]

    if len(set(weights_only)) == 1:
        return None

    freq = dd(int)
    for _, w, _ in name_weights:
        freq[w] += 1

    common_weight = None
    odd_weight = None
    for w, cnt in freq.items():
        if cnt == 1:
            odd_weight = w
        else:
            common_weight = w

    if common_weight is None:
        common_weight = max(freq.items(), key=lambda x: x[1])[0]

    odd_child = None
    for name, tot_w, own_w in name_weights:
        if tot_w == odd_weight:
            odd_child = (name, tot_w, own_w)
            break

    if odd_child is None:
        return None

    diff = common_weight - odd_child[1]
    corrected_weight = odd_child[2] + diff

    return corrected_weight


find_branch_weight(tree[root])

res = find_cause(tree[root])
print(res)
