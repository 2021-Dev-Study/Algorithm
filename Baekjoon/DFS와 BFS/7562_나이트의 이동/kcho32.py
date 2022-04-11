# 가장 가까운: BFS
from collections import deque
import sys

tc = int(input())
# dx 상하 dy 좌우
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
answer = []


def bfs():
    global flag, size

    while queue:
        x, y = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # print("hm", nx, ny)
            if nx <= -1 or nx >= size or ny <= -1 or ny >= size:
                break
        
            if graph[nx][ny] == 0 and visited[nx][ny] == False:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
                visited[nx][ny] = True

            if nx == dest[0] and ny == dest[1]:
                flag = True
                break
        if flag:
            break

for i in range(tc):
    size = int(sys.stdin.readline())
    graph = [[0 for i in range(size)] for j in range(size)]
    queue = deque([list(map(int, sys.stdin.readline().split()))])
    dest = list(map(int, sys.stdin.readline().split()))
    visited = [[False for i in range(size)] for j in range(size)]

    flag = False
    if queue[0] == dest:
        answer.append(0)
    else:
        bfs()
        answer.append(graph[dest[0]][dest[1]])

print("\n".join(list(map(str, answer))))