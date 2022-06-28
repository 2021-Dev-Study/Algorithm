# 다익스트라 문제
# 단, 다익스트라 연산 과정에서 연결된 노드를 방문하는 대신 상하좌우 좌표를 방문하면 됨
INF = int(1e9)
import sys
input = sys.stdin.readline
import heapq

def dijkstra(a, b):
    q = []
    visited[a][b] = graph[a][b]
    heapq.heappush(q, (graph[a][b],a,b))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        cost, x, y = heapq.heappop(q)
        if cost > visited[x][y]:
            continue
        for i in range(4): # 책이랑 이 부분만 다름
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                dist = cost + graph[nx][ny]
                if dist < visited[nx][ny]:
                    visited[nx][ny] = dist
                    heapq.heappush(q,(dist, nx,ny))


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        
        graph = []
        for _ in range(N):
            graph.append(list(map(int, input().split())))
        
        visited = [[INF]*(N) for _ in range(N)]

        dijkstra(0,0)

        print(visited[N-1][N-1])
        
        