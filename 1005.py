from itertools import combinations
from math import gcd, sqrt
a = int(input())
while a:
    s = set()
    total = 0
    coprime = 0
    for _ in range(a):
        s.add(int(input()))
    for (x, y) in combinations(list(s), 2):
        total += 1
        if gcd(x, y) == 1:
            coprime += 1
    try:
        print('{:.6f}'.format(sqrt(6 * total / coprime)))
    except ZeroDivisionError:
        print('No estimate for this data set.')
    a = int(input())
