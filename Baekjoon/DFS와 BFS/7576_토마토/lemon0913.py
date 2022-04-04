import sys
from collections import deque
if __name__ == "__main__":
    M, N = map(int, input().split())
    graph = [0]*N
    for i in range(N):
        graph[i] = list(map(int, sys.stdin.readline().split()))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([])
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append([i, j])

    def bfs():
        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append([nx, ny])
    bfs()

    result = 0
    for i in graph:
        for j in i:
            # 토마토가 모두 익지 않았다면
            if j == 0:
                print(-1)
                exit(0)
        result = max(result, max(i))

    print(result-1)

 
