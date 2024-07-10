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


def create_rule(info):
    letter = info[0]
    symbol = info[1]
    start, destination = info.split(':')
    num = int(start[2:])
    return {
        'letter': letter, 
        'symbol': symbol, 
        'num': num, 
        'destination': destination
    }

def get_input():
    # filename = './input.txt'
    filename ='./test.txt'
    with open(filename) as file: 
        contents = file.read()
        rules, input = contents.split('\n\n')

        rules = rules.split('\n')
        input = input.split('\n')

        workflows = {}
        for line in rules:
            name, rule = line.split('{')
            rule = rule.replace('}', '')
            rule = rule.split(',')
            line_rules = []
            for x in rule[:-1]:
                line_rules.append(create_rule(x))
            
            line_rules.append(rule[-1])
            workflows[name] = (line_rules)

        ratings = []
        for i in input:
            i = i.replace('{', '')
            i = i.replace('}', '')
            i = i.split(',')
            rating = dd(int)
            for letter in i:
                l, s = letter.split('=')
                rating[l] = int(s)
            
            ratings.append(rating)

        return workflows, ratings


workflows, inputs = get_input()
passing_rules = []
queue = []

def check_input_against_rule(input, workflow):
    print(workflow)
    letter = workflow['letter']
    input_letter_value = input[letter]

    if workflow['symbol'] == '>':
        passes = input_letter_value > workflow['num']
        
        if passes:
            destination = workflow['destination']
            if destination == 'A':
                passing_rules.append(input)
            elif destination != 'R':
                check_input_against_rule(input, workflows[destination])
    else:
        passes = input_letter_value < workflow['num']
        if passes:
            destination = workflow['destination']
            if destination == 'A':
                passing_rules.append(input)
            elif destination != 'R':
                check_input_against_rule(input, workflows[destination])
    
for input in inputs: 
    for workflow in workflows.values():    
        check_input_against_rule(input, workflow)

print(passing_rules)