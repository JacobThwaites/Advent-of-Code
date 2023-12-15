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
        for line in file: 
            return line

        return input 

input = get_input()

def increment(str):
    new_last_char = chr(ord(str[-1]) + 1)
    if new_last_char == '{':
        if len(str) == 1:
            return 'aa'
        return increment(str[:-1]) + 'a'

    return str[:-1] + new_last_char

def has_three_consecutive(str):
    for i, _ in enumerate(str[:-2]):
        if ord(str[i]) == ord(str[i+1]) - 1 and ord(str[i+1]) == ord(str[i+2]) - 1:
            return True
        
    return False

def has_invalid_chars(str):
    for char in str:
        if char in 'iol':
            print(char)
            return True
    
    return False

def count_overlapping_pairs(str):
    total = 0

    i = 0
    while i < len(str) - 1:
        print(str[i], str[i+1])
        if str[i] == str[i+1]:
            total += 1
            i+= 1
        
        i += 1
    
    return total
        

def is_valid(str):
    three_consecutive = has_three_consecutive(str)

    if not three_consecutive:
        return False
    
    if has_invalid_chars(str):
        return False
    
    overlapping_pairs = count_overlapping_pairs(str)

    if overlapping_pairs < 2:
        return False

    return True

password = input

while not is_valid(password):
    password = increment(password)

print(password)

password = increment(password)

while not is_valid(password):
    password = increment(password)

print(password)
