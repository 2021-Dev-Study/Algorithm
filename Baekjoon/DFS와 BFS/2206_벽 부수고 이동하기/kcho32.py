# 모든 벽을 하나씩 부숴보는 방법은 안됨

# from collections import deque
# from copy import deepcopy

# n, m = map(int, input().split())
# graph = [list(map(int, list(input()))) for i in range(n)]
# tmp_graph = deepcopy(graph)

# distance = []
# queue = deque([[0, 0]])
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs():
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
#                 continue

#             if tmp_graph[nx][ny] == 0:
#                 tmp_graph[nx][ny] = tmp_graph[x][y] + 1
#                 queue.append([nx, ny])

# bfs()
# distance.append(tmp_graph[n-1][m-1])

# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 1:
#             tmp_graph = deepcopy(graph)
#             tmp_graph[i][j] = 0
#             queue = deque([[0, 0]])
#             bfs()
#             distance.append(tmp_graph[n-1][m-1])
        

# if len(distance) == 1:
#     print(distance[0] + 1)
# else:
#     sorted_dist = sorted(list(set(distance)))
#     if len(sorted_dist) == 1:
#         if sorted_dist[0] == 0:
#             print(-1)
#         else:
#             print(sorted_dist[0])
#     else:
#         print(sorted_dist[1] + 1)

from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for i in range(n)]
tmp_graph = deepcopy(graph)

distance = []
queue = deque([[0, 0]])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]




def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue

            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = tmp_graph[x][y] + 1
                queue.append([nx, ny])