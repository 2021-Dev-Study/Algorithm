import sys

input = sys.stdin.readline
cities = int(input())
busses = int(input())
INF = int(1e9)
graph = [[INF for _ in range(cities + 1)] for __ in range(cities + 1)]

for i in range(1, cities + 1):
    for j in range(1, cities + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(busses):
    f, t, c = map(int, input().split())
    graph[f][t] = min(c, graph[f][t])

for k in range(1, cities + 1):
    for a in range(1, cities + 1):
        for b in range(1, cities + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, cities + 1):
    for b in range(1, cities + 1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
