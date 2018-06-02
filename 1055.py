a, b = [int(x) for x in input().split()]
if a > b:
    for x in range(a-b+1):
        print(*(['*'] * (a-x)), sep='')
else:
    for x in range(a, b+1):
        print(*(['*'] * x), sep='')
