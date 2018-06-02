from queue import Queue
run = True


def BFS(step, x, y, h):
    global run, ans
    if (x, y) in visited:
        return
    visited.add((x, y))
    if not (-1 < x < M and -1 < y < N) or abs(field[x][y]) - h > 5 or not run:
        return
    if x == (M-1) and y == (N-1):
        run = False
        ans = step
        return
    step += 1
    h = field[x][y]
    BFS_Queue.put((step, x+1, y, h))
    BFS_Queue.put((step, x, y+1, h))
    BFS_Queue.put((step, x-1, y, h))
    BFS_Queue.put((step, x, y-1, h))


a = int(input())
for _ in range(a):
    visited = set()
    BFS_Queue = Queue()
    run = True
    ans = 0
    M, N = [int(x) for x in input().split()]
    field = [[int(x) for x in input().split()] for n in range(M)]
    BFS_Queue.put((0, 0, 0, field[0][0]))
    while run and not BFS_Queue.empty():
        BFS(*BFS_Queue.get())
    print(ans)
