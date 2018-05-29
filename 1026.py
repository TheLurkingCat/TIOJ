from math import log2, ceil
a = int(input())
if a == 1:
    print('1\n+')
    exit()
t = ceil(log2(a))
b = 1 << t-1
print(t)
output = []
while True:
    if a > 0:
        a -= b
        output.append('+')
    elif a < 0:
        a += b
        output.append('-')
    else:
        break
    b >>= 1
print(*output[::-1], sep='')
