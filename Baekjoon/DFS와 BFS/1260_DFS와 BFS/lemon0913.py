import sys
from collections import deque
if __name__ == "__main__":
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)

    # 조건 중에 방문할 수 있는 정점이 여러개인 경우 정점 번호가 작은것을 먼저 방문한다고 함
    # -> graph를 정렬하는 과정이 필요
    for i in range(1, N+1):
        graph[i].sort()

    # dfs 함수 부분
    visited = [False] * (N+1)
    def dfs(v):
        visited[v] = True
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                dfs(i)
    
    dfs(V)
    print()

    # bfs 함수 부분
    visited = [False] * (N+1)
    def bfs(start):
        visited[start] = True
        queue = deque([start])

        while queue:
            v = queue.popleft()
            print(v, end = ' ')
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


    bfs(V)