from math import gcd
while True:
    a, b = [int(x) for x in input().split()]
    if a or b:
        print(gcd(a, b))
    else:
        break