while True:
    try:
        a = input()
    except EOFError:
        break
    print(*sorted([int(x) for x in input().split()]))
