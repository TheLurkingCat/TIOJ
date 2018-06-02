a = int(input())
while a:
    for x in range(a-1):
        out = '*' + ' ' * (a-x-2) + '*' + ' ' * (a-x-2) + '*'
        print(out.center(2*a-1))
    print('*' * (2 * a - 1))
    for x in range(a-1):
        out = '*' + ' ' * x + '*' + ' ' * x + '*'
        print(out.center(2*a-1))
    a = int(input())
