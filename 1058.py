from decimal import Decimal, getcontext
getcontext().prec = 1000
a, b = [Decimal(x) for x in input().split()]
print(max(a, b))
