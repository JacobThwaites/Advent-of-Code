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
        starts = []
        bots = {}
        for line in file:
            line = line.replace('\n', '')
            line = line.split(' ')

            if line[0] == 'value':
                start = {
                    'bot_id': int(line[-1]),
                    'value': int(line[1])
                }
                starts.append(start)
            else:
                bot = {
                    'id': int(line[1]),
                    'low_receiver_type': line[5],
                    'low_receiver_id': int(line[6]),
                    'high_receiver_type': line[-2],
                    'high_receiver_id': int(line[-1]),
                    'values': []
                }
                bots[int(line[1])] = bot

        return [starts, bots]

starts, bots = get_input()

outputs = dd(list)

for start in starts:
    id = start['bot_id']
    val = start['value']
    bots[id]['values'].append(val)


queue = []
for id, bot in bots.items():
    if len(bot['values']) > 1:
        queue.append(id)



def move_value(receiver_type, id, value):
    if receiver_type == 'output':
        outputs[id].append(value)
    else:
        bots[id]['values'].append(value)
        bots[id]['values'].sort()


while queue:
    bot_id = queue.pop(0)
    bot = bots[bot_id]

    if len(bot['values']) < 2:
        continue

    low = min(bot['values'])
    high = max(bot['values'])

    if low == 17 and high == 61:
        print(f'part 1: {bot_id}')

    bot['values'].clear()

    move_value(bot['low_receiver_type'], bot['low_receiver_id'], low)
    move_value(bot['high_receiver_type'], bot['high_receiver_id'], high)

    if bot['low_receiver_type'] == 'bot' and len(bots[bot['low_receiver_id']]['values']) == 2:
        queue.append(bot['low_receiver_id'])

    if bot['high_receiver_type'] == 'bot' and len(bots[bot['high_receiver_id']]['values']) == 2:
        queue.append(bot['high_receiver_id'])


print(f'part 2: {outputs[0][0] * outputs[1][0] * outputs[2][0]}')
