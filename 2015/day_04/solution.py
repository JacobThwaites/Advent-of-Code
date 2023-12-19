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

input = "iwrupvqb"

for x in range(10000000):
    h = hashlib.md5((input + str(x)).encode()).hexdigest()
    if h[:6] == '000000':
        print(x)
        break
