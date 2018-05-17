from datetime import datetime, timedelta
t1 = datetime(2000, 1, 1, *[int(x) for x in input().split(':')])
t2 = datetime(2000, 1, 1, *[int(x) for x in input().split(':')])
t3 = timedelta(days=1)
if t2 < t1:
    t2 += t3
print(t2 - t1)