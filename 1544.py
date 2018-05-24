try:
    a = int(input())
    for _ in range(a):
        x = input().strip()
        y = input().strip()
        if len(x) > len(y):
            print('0')
        else:
            print('0' if x > y else '1')
except Exception:
    pass