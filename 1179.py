a = [int(x) for x in input().split()]
while a != [0]:
    print(a[0], len(a)-1, sum(a))
    a = [int(x) for x in input().split()]
