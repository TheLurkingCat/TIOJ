n = int(input())
while n:
    k = sorted([int(x) for x in input().split()])
    floor = 1 + sum(k)
    floor += k[-1]
    print(floor)
    n = int(input())