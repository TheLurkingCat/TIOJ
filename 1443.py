a = int(input())
s = format(a, 'b')[1:]
Got = False
Zero = False
ans = 0
length = 0
for x in s:
    length += 1
    if Got:
        if not Zero and x == '0':
            Zero = True
        ans += 1
    elif x == '1':
        Got = True
        ans += 1
if not Zero:
    ans += 1
print(max(ans, length))
