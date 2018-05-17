a = int(input())
s = list(range(1, a+1))
while len(s) > 1:
    s = s[::2]
print(s[0])