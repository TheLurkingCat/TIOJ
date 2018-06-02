a = int(input())
for _ in range(a):
    greater = []
    smaller = []
    temp = input().strip()
    while not temp:
        temp = input().strip()
    x, y = [int(x) for x in temp.split()]
    for __ in range(x-1):
        t = int(input())
        if t > y:
            greater.append(t)
        else:
            smaller.append(t)
    print(min(greater), max(smaller))
