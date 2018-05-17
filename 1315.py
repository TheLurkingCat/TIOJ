a = int(input())
for _ in range(a):
    x, y, z = sorted([int(x) for x in input().split()])
    if x + y > z:
        if pow(x, 2) + pow(y, 2) == pow(z, 2):
            print('yes')
        else:
            print('no')
    else:
        print('no')