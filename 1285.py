while True:
    try:
        a, b = [int(x) for x in input().split()]
    except EOFError:
        break
    ans = 0
    if a < b:
        a, b = b, a
    while True:
        try:
            div, mod = divmod(a, b)
        except ZeroDivisionError:
            break
        ans += div
        a, b = b, mod
    print(ans)
