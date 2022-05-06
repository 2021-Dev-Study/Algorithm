import sys
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]


for _ in range(E) :
  a, b, c = map(int, input().split())
  graph[a].append([b, c])
  graph[b].append([a, c])

v1, v2 = map(int, input().split())
import heapq
def dijkstra(start) :
    dis = [1e9]*(N+1)
    q = []
    heapq.heappush(q, [0, start]) # [(총거리), (시작)]
    dis[start] = 0
    while q :
        move, now = heapq.heappop(q)
        if move > dis[now] :
            continue
        for child in graph[now] :
            now_m = move + child[1]
            if dis[child[0]] > now_m :
                dis[child[0]] = now_m
                heapq.heappush(q, [now_m, child[0]])
    return dis

one_start = dijkstra(1)
v1_start = dijkstra(v1)
v2_start = dijkstra(v2)

ans = min( one_start[v1] + v1_start[v2] + v2_start[N],
           one_start[v2] + v2_start[v1] + v1_start[N] )

print(ans if ans < 1e9 else -1)