while True:
    try:
        N, M = [int(x) for x in input().split()]
    except EOFError:
        break
    for x in range(1, N+1):
        output = []
        for y in range(1, M+1):
            output.append('{}*{}={}'.format(x, y, x*y))
        print(*output)