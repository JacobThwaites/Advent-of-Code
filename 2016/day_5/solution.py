import sys
import math
import bisect
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
import hashlib


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
            input.append(line)

        return input 

input = get_input()
[print(row) for row in input]

input = input[0]
    
password = ''
count = 0

# while len(password) < 8:
#     s = input + str(count)
    
#     hash = hashlib.md5(s.encode())
#     hex = hash.hexdigest()
#     if hex[0:5] == '00000':
#         # print(hex + " " + str(count))
#         password += hex[5]
    
#     count += 1
    
# print(password)

# Part 2

password = "________"

count = 0

while '_' in password:
    s = input + str(count)

    hash = hashlib.md5(s.encode())
    hex = hash.hexdigest()
    if hex[0:5] == '00000':
        if not hex[5].isdigit():
            pass
        elif int(hex[5]) >= len(password):
            pass
        elif password[int(hex[5])] == "_":
            pos = int(hex[5])
            char = hex[6]
            print(password)
            password = password[0:pos] + char + password[pos+1:]

    count += 1
print(password)