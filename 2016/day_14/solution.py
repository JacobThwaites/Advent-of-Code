import sys
import math
import bisect
import re
from math import gcd,floor,sqrt,log, prod
from collections import defaultdict as dd, deque
from bisect import bisect_left as bl, bisect_right as br
import hashlib

sys.setrecursionlimit(100000000)

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

mod=1000000007

# Test Input
# input = 'abc'

input = 'zpqevtbw'



def threes(hash) -> str:
    r = 2
    while r < len(hash):
        if hash[r] == hash[r-1] == hash[r-2]:
            return hash[r]
        r += 1
    return None

def fives(hash):
    letters = {}
    r = 4
    while r < len(hash):
        if hash[r] == hash[r-1] == hash[r-2] == hash[r-3] == hash[r-4]:
            letters[hash[r]] = True
        r += 1
    return letters


three_letter_occurrences = {}

indexes = {}
num = 1


while len(indexes) < 64:
    hash_val = hashlib.md5((input + str(num)).encode()).hexdigest()

    three_letter = threes(hash_val)
    if three_letter:
        three_letter_occurrences[num] = three_letter

    five_letters = fives(hash_val)
    if five_letters:
        for i in range(max(0, num - 1000), num):
            if i in three_letter_occurrences:
                if three_letter_occurrences[i] in five_letters:
                    indexes[i] = True

    num += 1

print(list(indexes.keys())[63])

# Part 2

def multihash(s, count=0):
    if count > 2016:
        return s

    s = hashlib.md5((s).encode()).hexdigest()
    return multihash(s, count+1)


assert multihash('abc0') == 'a107ff634856bb300138cac6568c0f24'

def part_2():
    indexes = {}
    three_letter_occurrences = {}
    prev_1000 = dd(list)

    num = 0
    while len(indexes) < 64:
        base_hash = hashlib.md5((input + str(num)).encode()).hexdigest()
        hash_val = multihash(base_hash)

        three_letter = threes(hash_val)
        if three_letter:
            three_letter_occurrences[num] = three_letter
            prev_1000[three_letter].append(num)

        for letter in list(prev_1000.keys()):
            prev_1000[letter] = [
                i for i in prev_1000[letter] if i > num - 1000]
            if not prev_1000[letter]:
                del prev_1000[letter]

        five_letters = fives(hash_val)
        if five_letters:
            for letter in five_letters:
                if letter in prev_1000:
                    for index in prev_1000[letter]:
                        indexes[index] = True
                        print(f'{index}, found {len(indexes)}')

        num += 1

    print(sorted(indexes.keys())[63])

part_2()