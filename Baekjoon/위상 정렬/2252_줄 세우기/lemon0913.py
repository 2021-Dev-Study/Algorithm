# 책이랑 똑같이 풀면 됨
from collections import deque
if __name__ == "__main__":
    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    
    result = []
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(i, end=' ')