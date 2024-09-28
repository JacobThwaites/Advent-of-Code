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
    if len(node['children'].values()) == 0:
        return weight
    
    for child in node['children'].values():
        weight += find_branch_weight(child)
        
    node['total_branch_weight'] = weight
    return weight

def are_branches_balanced(node):
    if len(node['children'].values()) == 0:
        return True
    
    weights = []
    comb = []
    
    for child in node['children'].values():
        weight = find_branch_weight(child)
        weights.append(weight)
        comb.append((child['name'], weight))
        
    for i, _ in enumerate(weights[1:]):
        if weights[i] != weights[i-1]:
            return False 
    
    return True

for child in tree[root]['children'].values():
    are_branches_balanced(child)
    
def find_odd_one_out(name_weights):
    totals = dd(int)
    
    for (name, weight) in name_weights:
        totals[weight] += 1
    print(totals)
    for w, count in totals.items():
        if count == 1:
            for (name, weight) in name_weights:
                if weight == w:
                    print(name, w)
                    return name

def find_cause(node):
    child_nodes = node['children'].values()
    if len(child_nodes) == 0:
        return 
    
    if len(child_nodes) < 2:
        for node in child_nodes:
            find_cause(node)
        
    if are_branches_balanced(node):
        for node in child_nodes:
            find_cause(node)
    else:
        name_weights = [(n['name'], n['total_branch_weight']) for n in node['children'].values()]
        odd = find_odd_one_out(name_weights)
        find_cause(node['children'][odd])


find_cause(tree[root])
    