s = []
win = 0
lose = 0
a = int(input())
for _ in range(a):
    t = int(input())
    if t <= 0:
        lose += 1
    else:
        win += 1
    s.append(abs(t))
s.sort()
del s[0]
del s[-1]
print('Average time: {:.3f} sec(s).'.format(sum(s) / len(s)))
print('Winning rate: {:.3f} %.'.format(win * 100 / (win + lose)))