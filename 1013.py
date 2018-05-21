from array import array
from queue import Queue
Dead = False
Visited = set()
BFS_Queue = Queue()
def BFS(T, Px, Py):
    print(T)
    if (Px, Py) in Visited:
        return None
    if map[Px][Py] == 'F':
        return None
    if Dead:
        return None
    Visited.add((Px, Py))
    BFS_Queue.put((T+1, Px+1, Py))
    BFS_Queue.put((T+1, Px-1, Py))
    BFS_Queue.put((T+1, Px, Py+1))
    BFS_Queue.put((T+1, Px, Py-1))
    fire_raging()
def fire_raging():
    global map, Dead
    for x in range(17):
        for y in range(10):
            try:
                if map[x][y] == 'F':
                    if map[x+1][y] == '.':
                        map[x+1][y] = 'F'
                    elif map[x+1][y] == 'E':
                        Dead = True
                    if map[x-1][y] == '.':
                        map[x-1][y] = 'F'
                    elif map[x-1][y] == 'E':
                        Dead = True
                    if map[x][y+1] == '.':
                        map[x][y+1] = 'F'
                    elif map[x][y+1] == 'E':
                        Dead = True
                    if map[x][y-1] == '.':
                        map[x][y-1] = 'F'
                    elif map[x][y-1] == 'E':
                        Dead = True
            except IndexError:
                pass
map = [list('*****************'), list('*...*.......**..*'), list('**..*....*.*.*..*'), list('*......*.**.**.**'), list('*..**...**..**.**'), list('**.....**..*.*..*'), list('*....*..........*'), list('*.....****.*...**'), list('****.*.*........*'), list('*****************')]
Fx, Fy = [int(x) for x in input().split()]
T = int(input())
Sx, Sy, Ex, Ey = [int(x) for x in input().split()]
map[Fx][Fy] = 'F'
map[Ex][Ey] = 'E'
for t in range(T):
    fire_raging()
BFS_Queue.put((T, Sx, Sy))
while not Dead or not BFS_Queue.empty():
    BFS(*BFS_Queue.get())