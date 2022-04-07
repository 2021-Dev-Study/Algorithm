from collections import deque

row, col = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(row)]
queue = deque([[0, 0]])
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bsf():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= row or ny <= -1 or ny >= col:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
        
bsf()
print(graph[row-1][col-1])
