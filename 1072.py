from operator import itemgetter
a = int(input())
while a:
    total = 0
    b = 0
    books = []
    for _ in range(a):
        books.append(tuple([int(x) for x in input().split()]))
    books.sort(key=itemgetter(1, 0), reverse=True)
    for x, y in books:
        total += x
        b = max(b, total+y)
    print(b)
    a = int(input())
