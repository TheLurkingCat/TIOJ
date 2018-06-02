N, M = [int(x) for x in input().split()]
cars = [int(x) for x in input().split()]
cars_in = [False] * (N+1)
stack = []
cache = []
pos = 0
for n in range(1, N+1):
    while not cars_in[n]:
        stack.append(cars[pos])
        cars_in[cars[pos]] = True
        pos += 1
    while stack[-1] != n and len(cache) < M:
        cache.append(stack.pop())
    t = stack.pop()
    if t != n:
        print('no')
        break
    cache.reverse()
    stack.extend(cache)
    cache.clear()
else:
    print('yes')
