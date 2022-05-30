# 작성자: red-Pen9uin
# 작성일: 2022-05-30
# Classification: DFS&BFS algorithm

from collections import deque
import sys
input = sys.stdin.readline # 편의상 지정

def bfs(max_time, N, graph):
    queue = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                queue.append((graph[i][j], i, j, 0))
    # print(queue)

    queue.sort()
    queue = deque(queue)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        virus, a, b, time = queue.popleft()
        if time == max_time:
            break
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((virus, nx, ny, time + 1))

    return graph


if __name__ == "__main__":
    N, K = map(int, input().split())
    graph = []
    for i in range(N):
        graph.append(list(map(int, input().split())))

    max_time, x, y = map(int, input().split())

    graph = bfs(max_time, N, graph)
    print(graph[x - 1][y - 1])