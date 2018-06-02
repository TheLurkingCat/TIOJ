h1, m1, s1 = [int(x) for x in input().split(':')]
h2, m2, s2 = [int(x) for x in input().split(':')]
h2 += 24
s2, m2, h2 = s2-s1, m2-m1, h2-h1
if s2 < 0:
    s2 += 60
    m2 -= 1
if m2 < 0:
    m2 += 60
    h2 -= 1
h2 %= 24
print('{:02d}:{:02d}:{:02d}'.format(h2, m2, s2))
