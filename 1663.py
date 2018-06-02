while True:
    try:
        t, a, b = [int(x) for x in input().split()]
    except EOFError:
        break
    if t == 1:
        print(a+b)
    elif t == 2:
        print(a-b)
    elif t == 3:
        print(a*b)
    else:
        print(a % b)
