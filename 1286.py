a, b, c, d = [int(x) for x in input().split()]
ans = 0
for _ in range((d-a) // b + 1):
    ans += pow(a, c, 1000000)
    a += b
print(ans % 1000000)
