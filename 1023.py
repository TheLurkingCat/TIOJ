while True:
    try:
        a = input()
    except EOFError:
        break
    ans = 0
    r = sorted([int(x) for x in input().split()])
    b = sorted([int(x) for x in input().split()])
    for x, y in zip(r, b):
        ans += x * y
    print(ans)
