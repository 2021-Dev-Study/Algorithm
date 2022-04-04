comp = int(input())
n = int(input())

graph = [[] for i in range(comp + 1)]
visited = [False] * (comp + 1)

for i in range(n):
    idx, dest = map(int, input().split())
    graph[idx].append(dest)
    # graph[dest].append(idx)

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)

print(visited.count(True) - 1)