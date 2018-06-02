a = int(input())
for _ in range(a):
    computers = []
    cost = 0
    temp = input().strip()
    while not temp:
        temp = input().strip()
    x, y = [int(x) for x in temp.split()]
    for __ in range(x):
        computers.append(tuple([int(x) for x in input().split()]))
        computers.sort()
    for com in computers:
        a = com[1]
        b = y - a
        t = a if b > 0 else y
        y = b
        cost += com[0] * t
        if y <= 0:
            break
    else:
        print('so sad')
        continue
    print(cost)
