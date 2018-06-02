from collections import Counter
n = int(input())
for _ in range(n):
    output = []
    a, b = input().split()
    k = Counter(b).most_common()
    temp = k[0][1]
    for x, y in k:
        if temp == y:
            output.append(x)
        else:
            break
    output.sort()
    print(*output, sep='')
