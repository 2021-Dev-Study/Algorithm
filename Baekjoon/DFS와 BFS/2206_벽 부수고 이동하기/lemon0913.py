from collections import deque

if __name__ == "__main__":
    N, M = map(int, input().split())

    graph = []
    for _ in range(N):
        graph.append(list(map(int, input())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1

    def bfs(a, b, c):
        queue = deque()
        queue.append((a,b,c))

        while queue:
            x, y, z = queue.popleft()
            
            # 끝 점에 도달하면 이동횟수를 출력
            if x == N-1 and y == M-1:
                return visited[x][y][z]
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 범위에서 벗어났다면 넘어가기
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                # 현재 위치가 벽이지만 아직 벽을 파괴한적이 없다면
                if graph[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))
                # 현재 위치기 벽이 아니면서 아직 한번도 방문하지 않은 곳이라면
                elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append((nx, ny, z))

        # 끝 점에 도달 못했다면
        return -1

    print(bfs(0, 0, 0)) 
