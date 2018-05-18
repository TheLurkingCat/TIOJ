while True:
    try:
        x = int(input())
    except EOFError:
        break
    ans = 0
    k = 1
    while x >= k:
        k *= 3
        ans += (x//k)
    print(ans)