import sys
from collections import deque
n, m, start = map(int, sys.stdin.readline().split())
arr= [[] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n+1)
for i in range(m):
    group, node = map(int, sys.stdin.readline().split())
    arr[group].append(node)
    arr[node].append(group)

for i in range(1, n+1):
    arr[i].sort()

def dfs(start):
    print(start , end = ' ')
    visited[start] = 1

    for i in arr[start]:
        if visited[i] == 0:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        q = queue.popleft()
        print(q, end=' ')
        for i in arr[q]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

            
dfs(start)
print()
visited = [0] * (n+1)
bfs(start)



