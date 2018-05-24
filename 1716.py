from math import sqrt
m = int(input())
for _ in range(m):
    a, b, c = [int(x) for x in input().split()]
    delta = b * b - 4 * a * c
    try:
        x = sqrt(delta)
    except ValueError:
        print('No')
        continue
    if x.is_integer():
        print('Yes')
    else:
        print('No')