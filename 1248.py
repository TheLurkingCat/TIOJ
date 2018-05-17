while True:
    try:
        a, op, b = input().split()
    except EOFError:
        break
    a, b = int(a), int(b)
    if a or b:
        if op == '+':
            print(a + b)
        elif op == '-':
            print(a - b)
        elif op == '*':
            print(a * b)
        else:
            print(*divmod(a, b), sep='...')
    else:
        break