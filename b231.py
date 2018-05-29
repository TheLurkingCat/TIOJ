from operator import itemgetter
while True:
    total = 0
    b = 0
    try:
        a = int(input())
    except EOFError:
        break
    books = []
    for _ in range(a):
        books.append(tuple([int(x) for x in input().split()]))
    books.sort(key=itemgetter(1, 0), reverse=True)
    for x, y in books:
        total += x
        b = max(b, total+y)
    print(b)