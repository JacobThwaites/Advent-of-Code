import sys
import math
import bisect
import re
import hashlib
from math import gcd,floor,sqrt,log, prod
from collections import defaultdict as dd, deque
from bisect import bisect_left as bl, bisect_right as br

sys.setrecursionlimit(100000000)

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

mod=1000000007


def get_input():
    filename = './input.txt'
    # filename ='./test.txt'
    with open(filename, 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            line = line.split()

            players = int(line[0])
            final_points = int(line[-2])
            return (players, final_points)


num_players, final_points = get_input()

player = 0

class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

    def insert(self, val):
        node = Node(val)
        node.prev = self

        node.next = self.next
        self.next.prev = node
        self.next = node

    def delete_next(self) -> int:
        deleted_val = self.next.val
        self.next.next.prev = self
        self.next = self.next.next

        return deleted_val

    def remove_seven_places_left(self):
        curr = self
        for _ in range(8):
            curr = curr.prev

        deleted = curr.delete_next()

        return curr.next, deleted

    def __str__(self):
        start = self.val
        output = f'{self.val}'

        curr = self.next
        while curr and curr.val != start:
            output += f', {curr.val}'
            curr = curr.next

        return output

curr = Node(0)
curr.next = curr
curr.prev = curr
player = 1
scores = dd(int)


final_points *= 100 # Part 2

for i in range(1, final_points+1):
    if i % 23 == 0:
        curr, deleted_val = curr.remove_seven_places_left()
        marble_value = deleted_val + i
        scores[player] += marble_value
    else:
        curr = curr.next
        curr.insert(i)
        curr = curr.next

    player += 1
    if player > num_players:
        player = 1

ans = max(v for v in scores.values())
print(ans)
