from math import gcd
a = int(input())
k = 0
for _ in range(a):
    if k == 1:
        break
    k = gcd(k, int(input()))
print(k)
