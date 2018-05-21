def Search(number, t):
    step = 0
    while number != t:
        if number > t:
            number //= 2
        else:
            t //= 2
        step += 1
    return step
a = int(input())
t = int(input())
ans = Search(a, t)
print(ans)