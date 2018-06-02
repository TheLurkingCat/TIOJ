from math import log
while True:
    try:
        a = int(input())
    except EOFError:
        break
    b = int(input())
    print(int(log(b, a)))
