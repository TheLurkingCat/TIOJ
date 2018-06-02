from itertools import permutations
n, r = [int(x) for x in input().split()]
s = []
for x in permutations(list(range(n)), r):
    temp = 0
    for i in range(r):
        temp += x[i] * pow(10, r-1-i)
    s.append(temp)
s.sort()
print(s[-n-r])