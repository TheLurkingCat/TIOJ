"""
Get TLE
"""
a = int(input())
for _ in range(a):
    x = input()
    t = int(input())
    for c in range(t):
        k = input()
        count = 0
        pos = 0
        while True:
            index = x.find(k, pos)
            if index >= 0:
                count += 1
                pos = index + 1
            else:
                break
        print(count)
