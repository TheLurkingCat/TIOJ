from queue import Queue
Hit = False
Stop = False
def BFS(x, y, z):
    global Hit, Stop
    if (x, y, z) in visited or Stop:
        return
    if not (-1 < x < n+1 and -1 < y < n+1):
        return
    if (x, y, z) == target:
        Hit = True
        Stop = True
        return
    visited.add((x, y, z))
    BFS_Queue.put((y, x, z))
    BFS_Queue.put((x, z, y))
    BFS_Queue.put((z, y, x))
    t1 = 2 * y - x + 1
    t2 = 2 * x - y - 1
    if -1 < t1 < n+1 and -1 < t2 < n+1:
        BFS_Queue.put((t1, t2, z))
n, x, y, z, *target = [int(x) for x in input().split()]
while n:
    BFS_Queue = Queue()
    visited = set()
    target = tuple(target)
    BFS(x, y, z)
    while not Stop and not BFS_Queue.empty():
        BFS(*BFS_Queue.get())
    print('Yes' if Hit else 'No')
    n, x, y, z, *target = [int(x) for x in input().split()]
