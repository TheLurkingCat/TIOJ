n, m = [int(x) for x in input().split()]
while n:
    ans = 1
    for x in range(n, n+m):
        ans *= x
    for x in range(2, m+1):
        ans //= x
    print(ans)
    n, m = [int(x) for x in input().split()]
