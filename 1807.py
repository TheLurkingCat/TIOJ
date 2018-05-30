a, b = [int(x) for x in input().split()]
dots = set()
for _ in range(b):
    x, y = [int(x) for x in input().split()]
    if (x, y) in dots or x == y:
        print('Yes')
        break
    else:
        dots.add((x, y))
        dots.add((y, x))
else:
    print('yes')