while True:
    temp = []
    try:
        a, k = [int(x) for x in input().split()]
    except EOFError:
        break
    for _ in range(a):
        temp.append(input())
    print(temp[-k])