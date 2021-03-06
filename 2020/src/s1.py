import collections
import itertools
import functools
import math
import re
import bisect
import random

rint = lambda: int(input())
rstr = lambda: input()
rints = lambda: list(map(int, input().split()))
rstrs = lambda: input().split()
wmat = lambda n, mat, sep: '{}\n{}'.format(n, '\n'.join(sep.join(map(str, row)) for row in mat))
warr = lambda n, arr, sep: '{}\n{}'.format(n, sep.join(map(str, arr)))
wl = lambda sep, *arr: sep.join(map(str, arr))

def main():
    n = rint()
    pairs = []
    for _ in range(n):
        pairs.append(rints())
    
    pairs.sort()
    ans = max(abs(pairs[i][1] - pairs[i-1][1]) / (pairs[i][0] - pairs[i-1][0]) for i in range(1, n)) 
    print(ans)
    
if __name__ == '__main__':
    main()
