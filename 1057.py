M, P, N = [int(x) for x in input().split()]
s = [int(x) for x in input().split()] + [P]
now = 0
pos = 0
step = 0
if M >= P:
    print('0')
    exit()
for x in s:
    if x <= M:
        pos = x
    else:
        break
while pos < P:
    if s[now] < pos:
        now += 1
    else:
        step += 1
        pos = s[now] + M
        now += 1
        if pos < s[now]:
            print('IMPOSSIBLE')
            exit()
print(step)
