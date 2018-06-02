from statistics import median_low, StatisticsError
m, n = [int(x) for x in input().split()]
x = []
y = []
for c in range(1, m+1):
    for i, k in enumerate([int(x) for x in input().split()], 1):
        y += [i] * k
        x += [c] * k
try:
    a = median_low(x)
except StatisticsError:
    a = 1
try:
    b = median_low(y)
except StatisticsError:
    b = 1
print(a, b)