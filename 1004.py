a = int(input())
s = list(range(1, a+1))
k = len(s)
while k > 1:
    if k & 1:
        s = s[::2]
        del s[0]
    else:
        s = s[::2]
    k = len(s)
print(s[0])
