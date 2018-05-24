a = int(input())
while a:
    s = [int(x) for x in input().split()]
    s.sort()
    print(*s)
    a = int(input())