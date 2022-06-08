# 작성자: red-Pen9uin
# 작성일: 2022-05-30
# Classification: DFS&BFS algorithm

import collections
import sys

input = sys.stdin.readline

n = int(input())
graph = [list(input().split()) for _ in range(n)]
dx,dy = [-1,1,0,0], [0,0,-1,1]
queue = collections.deque()
check = False

def bfs():
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'T':
                queue.append((i,j))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            temp_x, temp_y = x,y
            while True:
                nx = temp_x + dx[i]
                ny = temp_y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == 'X' and visited[nx][ny] == False:
                        visited[nx][ny] = True
                    elif graph[nx][ny] == 'S':
                        return False
                    elif graph[nx][ny] == 'O':
                        break
                    temp_x, temp_y = nx,ny
                else:
                    break
    return True

def recursive(index):
    global check
    if index == 3:
        if bfs():
            check = True
        return
        
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                recursive(index+1)
                graph[i][j] = 'X'

recursive(0)
if check:
    print("YES")
else:
    print("NO")