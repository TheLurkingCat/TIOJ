from math import gcd
from queue import Queue

BFS_Queue = Queue()
ans = None
StopFlag = False
def switch(n):
    global cups
    if n == 2:
        bfs2(0, '{} 0 {} 0'.format(*cups))
    elif n == 3:
        bfs3(0, '{} 0 {} 0 {} 0'.format(*cups))
    elif n == 4:
        bfs4(0, '{} 0 {} 0 {} 0 {} 0'.format(*cups))
    else:
        bfs5(0, '{} 0 {} 0 {} 0 {} 0 {} 0'.format(*cups))

def move(a, b, pos):
    a, b = int(a), int(b)
    max_b = cups[pos]
    b += a
    a = 0
    if b > max_b:
        a += b - max_b
        b = max_b
    return a, b

def bfs2(step, state):
    _, a, _, b = state.split()
    global StopFlag, ans
    if StopFlag:
        return None
    if state in used_state:
        return None
    if t == int(a) or t == int(b):
        StopFlag = True
        ans = step
        return None
    used_state.add(state)
    BFS_Queue.put((step+1, '{0} {0} {1} {2}'.format(*cups, b)))
    BFS_Queue.put((step+1, '{0} {2} {1} {1}'.format(*cups, a)))
    BFS_Queue.put((step+1, '{0} {3} {1} {2}'.format(*cups, b, 0)))
    BFS_Queue.put((step+1, '{0} {2} {1} {3}'.format(*cups, a, 0)))
    BFS_Queue.put((step+1, '{0} {2} {1} {3}'.format(*cups, *move(a, b, 1))))
    BFS_Queue.put((step+1, '{0} {3} {1} {2}'.format(*cups, *move(b, a, 0))))

def bfs3(step, state):
    _, a, _, b, _, c = state.split()
    global StopFlag, ans
    if StopFlag:
        return None
    if state in used_state:
        return None
    if t == int(a) or t == int(b) or t == int(c):
        StopFlag = True
        ans = step
        return None
    used_state.add(state)
    BFS_Queue.put((step+1, '{0} {0} {1} {3} {2} {4}'.format(*cups, b, c)))
    BFS_Queue.put((step+1, '{0} {3} {1} {1} {2} {4}'.format(*cups, a, c)))
    BFS_Queue.put((step+1, '{0} {3} {1} {4} {2} {2}'.format(*cups, a, b)))
    BFS_Queue.put((step+1, '{0} {5} {1} {3} {2} {4}'.format(*cups, b, c, 0)))
    BFS_Queue.put((step+1, '{0} {3} {1} {5} {2} {4}'.format(*cups, a, c, 0)))
    BFS_Queue.put((step+1, '{0} {3} {1} {4} {2} {5}'.format(*cups, a, b, 0)))
    BFS_Queue.put((step+1, '{0} {3} {1} {4} {2} {5}'.format(*cups, *move(a, b, 1), c)))
    BFS_Queue.put((step+1, '{0} {3} {1} {4} {2} {5}'.format(*cups, *move(b, a, 0), c)))
    BFS_Queue.put((step+1, '{0} {3} {1} {5} {2} {4}'.format(*cups, *move(a, c, 2), b)))
    BFS_Queue.put((step+1, '{0} {3} {1} {5} {2} {4}'.format(*cups, *move(c, a, 0), b)))
    BFS_Queue.put((step+1, '{0} {5} {1} {3} {2} {4}'.format(*cups, *move(b, c, 2), a)))
    BFS_Queue.put((step+1, '{0} {5} {1} {3} {2} {4}'.format(*cups, *move(c, b, 1), a)))

def bfs4(step, state):
    _, a, _, b, _, c, _, d = state.split()
    global StopFlag, ans
    if StopFlag:
        return None
    if state in used_state:
        return None
    if t == int(a) or t == int(b) or t == int(c) or t == int(d):
        StopFlag = True
        ans = step
        return None
    used_state.add(state)
    BFS_Queue.put((step+1, '{0} {0} {1} {4} {2} {5} {3} {6}'.format(*cups, b, c, d)))
    BFS_Queue.put((step+1, '{0} {4} {1} {1} {2} {5} {3} {6}'.format(*cups, a, c, d)))
    BFS_Queue.put((step+1, '{0} {4} {1} {5} {2} {2} {3} {6}'.format(*cups, a, b, d)))
    BFS_Queue.put((step+1, '{0} {4} {1} {5} {2} {6} {3} {3}'.format(*cups, a, b, c)))
    BFS_Queue.put((step+1, '{0} {7} {1} {4} {2} {5} {3} {6}'.format(*cups, b, c, d, 0)))
    BFS_Queue.put((step+1, '{0} {4} {1} {7} {2} {5} {3} {6}'.format(*cups, a, c, d, 0)))
    BFS_Queue.put((step+1, '{0} {4} {1} {5} {2} {7} {3} {6}'.format(*cups, a, b, d, 0)))
    BFS_Queue.put((step+1, '{0} {4} {1} {5} {2} {6} {3} {7}'.format(*cups, a, b, c, 0)))
    BFS_Queue.put((step+1, '{0} {4} {1} {5} {2} {6} {3} {7}'.format(*cups, *move(a, b, 1), c, d)))
    BFS_Queue.put((step+1, '{0} {4} {1} {5} {2} {6} {3} {7}'.format(*cups, *move(b, a, 0), c, d)))
    BFS_Queue.put((step+1, '{0} {4} {1} {6} {2} {5} {3} {7}'.format(*cups, *move(a, c, 2), b, d)))
    BFS_Queue.put((step+1, '{0} {4} {1} {6} {2} {5} {3} {7}'.format(*cups, *move(c, a, 0), b, d)))
    BFS_Queue.put((step+1, '{0} {6} {1} {4} {2} {5} {3} {7}'.format(*cups, *move(b, c, 2), a, d)))
    BFS_Queue.put((step+1, '{0} {6} {1} {4} {2} {5} {3} {7}'.format(*cups, *move(c, b, 1), a, d)))
    BFS_Queue.put((step+1, '{0} {4} {1} {6} {2} {7} {3} {5}'.format(*cups, *move(a, d, 3), b, c)))
    BFS_Queue.put((step+1, '{0} {4} {1} {6} {2} {7} {3} {5}'.format(*cups, *move(d, a, 0), b, c)))
    BFS_Queue.put((step+1, '{0} {6} {1} {4} {2} {7} {3} {5}'.format(*cups, *move(b, d, 3), a, c)))
    BFS_Queue.put((step+1, '{0} {6} {1} {4} {2} {7} {3} {5}'.format(*cups, *move(d, b, 1), a, c)))
    BFS_Queue.put((step+1, '{0} {6} {1} {7} {2} {4} {3} {5}'.format(*cups, *move(c, d, 3), a, b)))
    BFS_Queue.put((step+1, '{0} {6} {1} {7} {2} {4} {3} {5}'.format(*cups, *move(d, c, 2), a, b)))

def bfs5(step, state):
    _, a, _, b, _, c, _, d, _, e = state.split()
    global StopFlag, ans
    if StopFlag:
        return None
    if state in used_state:
        return None
    if t == int(a) or t == int(b) or t == int(c) or t == int(d) or t == int(e):
        StopFlag = True
        ans = step
        return None
    used_state.add(state)
    BFS_Queue.put((step+1, '{0} {0} {1} {5} {2} {6} {3} {7} {4} {8}'.format(*cups, b, c, d, e)))
    BFS_Queue.put((step+1, '{0} {5} {1} {1} {2} {6} {3} {7} {4} {8}'.format(*cups, a, c, d, e)))
    BFS_Queue.put((step+1, '{0} {5} {1} {6} {2} {2} {3} {7} {4} {8}'.format(*cups, a, b, d, e)))
    BFS_Queue.put((step+1, '{0} {5} {1} {6} {2} {7} {3} {3} {4} {8}'.format(*cups, a, b, c, e)))
    BFS_Queue.put((step+1, '{0} {5} {1} {6} {2} {7} {3} {8} {4} {4}'.format(*cups, a, b, c, d)))
    BFS_Queue.put((step+1, '{0} {9} {1} {5} {2} {6} {3} {7} {4} {8}'.format(*cups, b, c, d, e, 0)))
    BFS_Queue.put((step+1, '{0} {5} {1} {9} {2} {6} {3} {7} {4} {8}'.format(*cups, a, c, d, e, 0)))
    BFS_Queue.put((step+1, '{0} {5} {1} {6} {2} {9} {3} {7} {4} {8}'.format(*cups, a, b, d, e, 0)))
    BFS_Queue.put((step+1, '{0} {5} {1} {6} {2} {7} {3} {9} {4} {8}'.format(*cups, a, b, c, e, 0)))
    BFS_Queue.put((step+1, '{0} {5} {1} {6} {2} {7} {3} {8} {4} {9}'.format(*cups, a, b, c, d, 0)))
    BFS_Queue.put((step+1, '{0} {5} {1} {6} {2} {7} {3} {8} {4} {9}'.format(*cups, *move(a, b, 1), c, d, e)))
    BFS_Queue.put((step+1, '{0} {5} {1} {6} {2} {7} {3} {8} {4} {9}'.format(*cups, *move(b, a, 0), c, d, e)))
    BFS_Queue.put((step+1, '{0} {5} {1} {7} {2} {6} {3} {8} {4} {9}'.format(*cups, *move(a, c, 2), b, d, e)))
    BFS_Queue.put((step+1, '{0} {5} {1} {7} {2} {6} {3} {8} {4} {9}'.format(*cups, *move(c, a, 0), b, d, e)))
    BFS_Queue.put((step+1, '{0} {7} {1} {5} {2} {6} {3} {8} {4} {9}'.format(*cups, *move(b, c, 2), a, d, e)))
    BFS_Queue.put((step+1, '{0} {7} {1} {5} {2} {6} {3} {8} {4} {9}'.format(*cups, *move(c, b, 1), a, d, e)))
    BFS_Queue.put((step+1, '{0} {5} {1} {7} {2} {8} {3} {6} {4} {9}'.format(*cups, *move(a, d, 3), b, c, e)))
    BFS_Queue.put((step+1, '{0} {5} {1} {7} {2} {8} {3} {6} {4} {9}'.format(*cups, *move(d, a, 0), b, c, e)))
    BFS_Queue.put((step+1, '{0} {7} {1} {5} {2} {8} {3} {6} {4} {9}'.format(*cups, *move(b, d, 3), a, c, e)))
    BFS_Queue.put((step+1, '{0} {7} {1} {5} {2} {8} {3} {6} {4} {9}'.format(*cups, *move(d, b, 1), a, c, e)))
    BFS_Queue.put((step+1, '{0} {7} {1} {8} {2} {5} {3} {6} {4} {9}'.format(*cups, *move(c, d, 3), a, b, e)))
    BFS_Queue.put((step+1, '{0} {7} {1} {8} {2} {5} {3} {6} {4} {9}'.format(*cups, *move(d, c, 2), a, b, e)))
    BFS_Queue.put((step+1, '{0} {5} {1} {7} {2} {8} {3} {9} {4} {6}'.format(*cups, *move(a, e, 4), b, c, d)))
    BFS_Queue.put((step+1, '{0} {5} {1} {7} {2} {8} {3} {9} {4} {6}'.format(*cups, *move(e, a, 0), b, c, d)))
    BFS_Queue.put((step+1, '{0} {7} {1} {5} {2} {8} {3} {9} {4} {6}'.format(*cups, *move(b, e, 4), a, c, d)))
    BFS_Queue.put((step+1, '{0} {7} {1} {5} {2} {8} {3} {9} {4} {6}'.format(*cups, *move(e, b, 1), a, c, d)))
    BFS_Queue.put((step+1, '{0} {7} {1} {8} {2} {5} {3} {9} {4} {6}'.format(*cups, *move(c, e, 4), a, b, d)))
    BFS_Queue.put((step+1, '{0} {7} {1} {8} {2} {5} {3} {9} {4} {6}'.format(*cups, *move(e, c, 2), a, b, d)))
    BFS_Queue.put((step+1, '{0} {7} {1} {8} {2} {9} {3} {5} {4} {6}'.format(*cups, *move(d, e, 4), a, b, c)))
    BFS_Queue.put((step+1, '{0} {7} {1} {8} {2} {9} {3} {5} {4} {6}'.format(*cups, *move(e, d, 3), a, b, c)))


used_state = set()
n = int(input())
cups = []
k = 0
for x in input().split():
    k = gcd(k, int(x))
    cups.append(int(x))
max_cup = max(cups)
t = int(input())
if t > max_cup or t % k:
    print('-1')
    exit()
if n == 1:
    print(t // cups[0])
else:
    switch(n)
    while not StopFlag or not BFS_Queue.empty() :
        if n == 2:
            bfs2(*BFS_Queue.get())
        elif n == 3:
            bfs3(*BFS_Queue.get())
        elif n == 4:
            bfs4(*BFS_Queue.get())
        else:
            bfs5(*BFS_Queue.get())
    if ans is not None:
        print(ans)
    else:
        print('-1')