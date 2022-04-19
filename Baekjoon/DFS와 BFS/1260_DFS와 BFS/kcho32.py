from collections import deque


n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

for i in range(m):
    idx, dest = map(int, input().split())
    graph[idx].append(dest)
    graph[dest].append(idx)
    graph[idx].sort()
    graph[dest].sort()

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(graph, visited, start):
    visited[start] = True
    print(start, end = " ")

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, visited, i)

dfs(graph, visited_dfs, v)
print()
bfs(graph, visited_bfs, v)
