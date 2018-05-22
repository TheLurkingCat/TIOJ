from math import acos, sqrt, pi
while True:
    try:
        x, h, r = [float(x) for x in input().split()]
    except EOFError:
        break
    if h <= -r:
        print('0.00')
    elif h >= r:
        print('{:.2f}'.format(r * r * pi))
    else:
        print('{:.2f}'.format(r * r * (pi - acos(h / r)) + sqrt(r * r - h * h) * h))