dp = [[0] * 17, [0] * 17]
n, m = [int(x) for x in input().split()]
now = 0
previous = 1
dp[0][0:n+1] = [1] * (n+1)
for _ in range(m):
    now, previous = previous, now
    for i in range(n+1):
        dp[now][i] = dp[previous][i+1] + dp[previous][0]
print(dp[now][0])
