from operator import itemgetter
while True:
    money = 100
    account = []
    try:
        a = input()
    except EOFError:
        break
    a = int(input())
    if a == 0:
        print('No one')
        continue
    for _ in range(a):
        account.append((input().strip(), money))
        money -= 10
    account.sort(key=itemgetter(0))
    for x, y in account:
        print('{:<}  ${}'.format(x, y))
