"""
Unknown WA @ testdata 0
"""
from queue import Queue
NewFire = set()
Visited = set()
Stop = False
BFS_Queue = Queue()
ans = 'Help!'
t = 0
def BFS(T, Px, Py):
    global ans, Stop, t
    if (Px, Py) in Visited:
        return None
    if (map[Px][Py] == 'F' and not (Px, Py) in NewFire) or map[Px][Py] == '*':
        return None
    if map[Px][Py] == 'E':
        ans = T
        Stop = True
    T += 1
    Visited.add((Px, Py))
    BFS_Queue.put((T, Px+1, Py))
    BFS_Queue.put((T, Px-1, Py))
    BFS_Queue.put((T, Px, Py+1))
    BFS_Queue.put((T, Px, Py-1))
    if t != T:
        BFS_Queue.put('Fire')
        t += 1
def fire_raging():
    global map
    NewFire.clear()
    for x in range(10):
        for y in range(17):
            if map[x][y] == 'F' and not (x, y) in NewFire:
                try:
                    if map[x+1][y] == '.':
                        map[x+1][y] = 'F'
                        NewFire.add((x+1, y))
                except IndexError:
                    pass
                try:
                    if map[x-1][y] == '.':
                        map[x-1][y] = 'F'
                        NewFire.add((x-1, y))
                except IndexError:
                    pass
                try:
                    if map[x][y+1] == '.':
                        map[x][y+1] = 'F'
                        NewFire.add((x, y+1))
                except IndexError:
                    pass
                try:
                    if map[x][y-1] == '.':
                        map[x][y-1] = 'F'
                        NewFire.add((x, y-1))
                except IndexError:
                    pass
map = [list('*****************'), list('*...*.......**..*'), list('**..*....*.*.*..*'), list('*......*.**.**.**'), list('*..**...**..**.**'), list('**.....**..*.*..*'), list('*....*..........*'), list('*.....****.*...**'), list('****.*.*........*'), list('*****************')]
Fx, Fy = [int(x) for x in input().split()]
T = int(input())
Sx, Sy, Ex, Ey = [int(x) for x in input().split()]
map[Fx][Fy] = 'F'
map[Ex][Ey] = 'E'
for t in range(T-1):
    fire_raging()
BFS_Queue.put('Fire')
BFS(0, Sx, Sy)
while not BFS_Queue.empty() and not Stop:
    temp = BFS_Queue.get()
    if temp == 'Fire':
        fire_raging()
    else:
        BFS(*temp)
print(ans)