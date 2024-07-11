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

def find_closing_bracket(input, i):
    while i < len(input):
        if input[i] == ')':
            return i
        i += 1
    
    return -1

def format_input(input):
    output = {'mains': [], 'brackets': []}
    curr = ''
    marker_seen = False
    countdown = 0 
    i = 0
    while i < len(input):
        if countdown:
            curr += input[i]
            countdown -= 1
            i += 1
        elif input[i] == '(':
            output['mains'].append(curr)
            curr = ''
            closing_bracket_index = find_closing_bracket(input, i)
            l, r = input[i+1:closing_bracket_index].split('x')
            countdown = int(l)
            output['brackets'].append((int(l), int(r)))
            i += closing_bracket_index - i + 1
        else:
            curr += input[i]
            i += 1
    if curr:
        output['mains'].append(curr)
    
    return output
            
def get_input():
    filename = './input.txt'
    # filename ='./test.txt'
    with open(filename, 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            # return format_input(line)
            return line


input = get_input()
# print(input)

def generate(input):
    output = input['mains'][0]
    
    for i, (length, repeats) in enumerate(input['brackets']):
        main = input['mains'][i+1]
        l = main[:length]
        r = main[length:]
        for _ in range(repeats):
            output += l

        output += r
        
    return output

# solution = len(generate(input))
# print(solution)


# Part 2

def decompress(string):
    total = 0
    
    i = 0
    while i < len(string):
        char = string[i]
        if char != '(':
            total += 1
            i += 1
        else:
            closing_bracket_index = find_closing_bracket(string, i)
            length, copies = string[i+1:closing_bracket_index].split('x')
            compression_total = decompress(
                string[closing_bracket_index + 1:closing_bracket_index + 1 + int(length)])
            total += compression_total * int(copies)
            i = closing_bracket_index + int(length) + 1
    
    return total 

print(decompress(input))