from decimal import Decimal
a = int(input())
while a:
    s = sorted([Decimal(x) for x in input().split()])
    del s[0]
    del s[-1]
    print('{:.2f}'.format(sum(s) / (a-2)))
    a = int(input())
