"""
각각에서 익은 토마토(1)이 있으면 bfs 시작 -> 다음에 방문한 곳은 그 전의 방문한 값 + 1
bfs에서 -1, 1이 아니고 더 작은 값이 나오면 작은 값으로 교체 : 더 빠른 시간에 영향을 주기 때문
bfs 끝나면 max값 찾기?
"""
from collections import deque

# y: column, x: row
cols, rows = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(rows)]
days = {}
flag = False

queue = deque()

# 바로 연결되어 있는 토마토들을 이전의 값 + 1로 두어 순서 표시
# 다른 토마토에서 더 빠른 영향을 주는 거면(값이 더 낮게 나오면) 교체
def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                continue

            if graph[nx][ny] == 0 or graph[nx][ny] > graph[x][y] + 1:
                graph[nx][ny] = graph[x][y] + 1 # 2 저장
                queue.append((nx, ny))
                days[(nx, ny)] = graph[nx][ny]


for i in range(rows):
    for j in range(cols):
        days[(i, j)] = graph[i][j]
        if graph[i][j] == 1:
            queue.append([i, j])

bfs()

days = set(days.values())
    
if 0 in days:
    print(-1)
else:
    print(max(days) -1)
