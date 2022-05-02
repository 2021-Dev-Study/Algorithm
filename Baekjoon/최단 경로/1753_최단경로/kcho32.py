import sys
import heapq

input = sys.stdin.readline
nodes, roads = map(int, input().split())
start = int(input())
graph = [[] for _ in range(nodes + 1)]
INF = int(1e9)
visited = [False for _ in range(nodes + 1)]
dist = [INF for _ in range(nodes + 1)]

for i in range(roads):
    f, t, c = map(int, input().split())
    graph[f].append((t, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue
        for j in graph[now]:
            c = distance + j[1]
            if c < dist[j[0]]:
                dist[j[0]] = c
                heapq.heappush(q, (c, j[0]))

dijkstra(start)

for i in range(1, nodes + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])