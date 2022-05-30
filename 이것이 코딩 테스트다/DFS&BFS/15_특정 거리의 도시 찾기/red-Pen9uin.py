# 작성자: red-Pen9uin
# 작성일: 2022-05-30
# Classification: DFS&BFS algorithm

from collections import deque
import sys
input = sys.stdin.readline # 편의상 지정

def bfs(start, N, graph):
    distance = [0] * (N+1)
    visited = [False] * (N+1)
    answer = []

    queue = deque([start])
    visited[start] = True
    distance[start] = 0

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == K:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i)


if __name__ == "__main__":
    N, M, K, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]


    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)

    bfs(X, N, graph)