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
    filename ='./test.txt'
    with open(filename, 'r') as file: 
        input = []
        for line in file: 
            line = line.replace('\n', '')
            line = line.split(' ')
            instruction = []
            if line[0] == 'value':
                instruction.append(line[0])
                instruction.append(int(line[1]))
                instruction.append(line[-2])
                instruction.append(int(line[-1]))
            else:
                instruction.append(line[0])
                instruction.append(int(line[1]))
                instruction.append(line[3])
                instruction.append(line[5])
                instruction.append(int(line[6]))
                instruction.append(line[8])
                instruction.append(line[-2])
                instruction.append(int(line[-1]))
            input.append(instruction)

        return input 

input = get_input()
# [print(row) for row in input]

bots = {}
bots = dd(list)
outputs = {}
for row in input:
    if row[0] == 'value':
        bot_id = row[-1]
        print('bot id' + str(bot_id))
        if bot_id not in bots:
            bots[bot_id] = []
        bots[bot_id].append(row[1])
        bots[bot_id].sort()
    else:
        giver_id = row[1]
        # if giver_id not in bots:
        #     bots[giver_id] = []
        print(bots)
        print('giver_id: ' + str(giver_id))
        
        low = bots[giver_id].pop(0) if row[2] == 'low' else bots[giver_id].pop()
        high = bots[giver_id].pop()
        
        receiver_id = row[4]
        if row[3] == 'output':
            if receiver_id not in outputs:
                outputs[receiver_id] = []
                
            outputs[receiver_id].append(low) if row[2] == 'low' else outputs[receiver_id].append(high)
        else:
            if receiver_id not in bots:
                bots[receiver_id] = []
            bots[receiver_id].append(low) if row[2] == 'low' else bots[receiver_id].append(high)

for bot in bots:
    print(bot)