INF = int(1e9)
import sys
input = sys.stdin.readline
import heapq

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append((b,1))
        graph[b].append((a,1))

    visited = [INF]*(N+1)

    def dijkstra(start):
        q = []
        visited[start] = 0
        heapq.heappush(q,(0,start))

        while q:
            cost, now = heapq.heappop(q)

            if cost > visited[now]:
                continue

            for x in graph[now]:
                dist = cost + x[1]
                if dist < visited[x[0]]:
                    visited[x[0]] = dist
                    heapq.heappush(q,(dist,x[0]))
    
    dijkstra(1)
    
    m = 0
    idx = 0
    for i in range(1,N+1):
        if visited[i] > m:
            m = visited[i]
            idx = i
    print(m, idx, visited.count(m))