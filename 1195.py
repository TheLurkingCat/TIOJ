a = int(input())
ans = 0
for _ in range(a):
    x = input()[2:]
    c = x[1]
    if x.count(c) == 4:
        ans += 2000
    elif x[1:].count(c) == 3 or x[:3].count(c) == 3:
        ans += 1000
    else:
        ans += 1500
print(ans)
