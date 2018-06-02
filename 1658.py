while True:
    output = []
    try:
        N, B = [int(x) for x in input().split()]
    except EOFError:
        break
    if B:
        for x in range(1, 2*N, 2):
            output.append('*' * x)
    else:
        for x in range(1, 2*N, 2):
            if x == 1:
                output.append('*')
            elif x == 2 * N - 1:
                output.append('*' * x)
            else:
                output.append('* *')
    print(*output, sep='\n')
