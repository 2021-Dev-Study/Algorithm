"""
각각에서 익은 토마토(1)이 있으면 bfs 시작 -> 다음에 방문한 곳은 그 전의 방문한 값 + 1
bfs에서 -1, 1이 아니고 더 작은 값이 나오면 작은 값으로 교체 : 더 빠른 시간에 영향을 주기 때문
bfs 끝나면 max값 찾기?
"""
from collections import deque


cols, rows, heights = map(int, input().split())
graph = [list(list(map(int, input().split())) for _ in range(rows)) for __ in range(heights)]
days = {}

queue = deque()

# 바로 연결되어 있는 토마토들을 이전의 값 + 1로 두어 순서 표시
# 다른 토마토에서 더 빠른 영향을 주는 거면(값이 더 낮게 나오면) 교체
def bfs():
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or ny < 0 or nz < 0 or nx >= rows or ny >= cols or nz >= heights:
                continue

            if graph[nz][nx][ny] == 0 or graph[nz][nx][ny] > graph[z][x][y] + 1:
                graph[nz][nx][ny] = graph[z][x][y] + 1 # 2 저장
                queue.append((nz, nx, ny))
                days[(nz, nx, ny)] = graph[nz][nx][ny]

for z in range(heights):
    for i in range(rows):
        for j in range(cols):
            days[(z, i, j)] = graph[z][i][j]
            if graph[z][i][j] == 1:
                queue.append([z, i, j])

bfs()

days = set(days.values())
    
if 0 in days:
    print(-1)
else:
    print(max(days) -1)
