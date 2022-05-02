import heapq
import sys
input = sys.stdin.readline

E, V = map(int, input().split())
start = int(input())

graph = [[] for _ in range(E+1)]
dis = [1e9]*(E+1)

for _ in range(V) :
    u, v, w = map(int, input().split())
    graph[u].append([v,w])

q = []
heapq.heappush(q, [0, start])
dis[start] = 0

while q :
    total_w, now = heapq.heappop(q)
    if dis[now] < total_w :
        continue
    for child in graph[now] :
        weight = total_w + child[1]
        if weight < dis[child[0]] :
            dis[child[0]] = weight
            heapq.heappush(q, [weight, child[0]])
for i in range(1, E+1) :
    if dis[i] == 1e9 :
        print("INF")
    else :
        print(dis[i])