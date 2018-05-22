a, b = sorted([int(x) for x in input().split()])
while a or b:
    ans = a * (a + 1) * (b + 1) - (a + b + 2) * (a * a + a) // 2 + a * (a + 1) * (2 * a + 1) // 6
    print(ans)
    a, b = sorted([int(x) for x in input().split()])