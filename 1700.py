from math import gcd
from functools import reduce
while True:
    try:
        a = input()
    except EOFError:
        break
    s = [int(x) for x in input().split()]
    print(reduce(gcd, s))
