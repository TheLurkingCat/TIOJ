from decimal import Decimal, getcontext, ROUND_HALF_UP
getcontext().prec = 100
# .quantize(Decimal('1'), rounding=ROUND_HALF_UP)
s, t, n, *seat = [Decimal(x) for x in input().split()]
income = 0
cost = (s * t * 3 / 10).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
k = sum(seat)
t20 = (t / 5).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
t40 = (t * 2 / 5).quantize(Decimal('1'), rounding=ROUND_HALF_UP) - t20
t60 = (t * 3 / 5).quantize(Decimal('1'), rounding=ROUND_HALF_UP) - t20 - t40
s70 = (s * 7 / 10).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
s80 = (s * 4 / 5).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
s90 = (s * 9 / 10).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
if k >= t20:
    k -= t20
    income += (t20 * s70)
    if k >= t40:
        k -= t40
        income += (t40 * s80)
        if k >= t60:
            k -= t60
            income += (t60 * s90)
            if k > 0:
                income += (k * s)
        else:
            income += k * s90
    else:
        income += k * s80
else:
    income += k * s70
income -= cost
print(income)
