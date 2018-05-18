from decimal import Decimal
a1 = Decimal(input())
a2 = Decimal(input())
b1 = Decimal(input())
b2 = Decimal(input())
k = a1 - a2
c = b2 - b1
x = c / k
y = a1 * x + b1
if not x:
    x = Decimal('0.00')
if not y:
    y = Decimal('0.00')
print('{:.2f}'.format(x))
print('{:.2f}'.format(y))