# import sys
# if __name__ == "__main__":

#     def dfs(x, y):
#         # 탐색 중에 범위를 벗어날 경우 종료
#         if x <= -1 or y <= -1 or y >= N or x >= M:
#             return False
#         # 현재 노드가 방문할 수 있는 위치라면
#         if graph[x][y] == 1:
#             # 이제 해당 노드는 방문할 수 없는 위치로 교체
#             graph[x][y] = 0
#             dfs(x-1, y)
#             dfs(x+1, y)
#             dfs(x, y+1)
#             dfs(x, y-1)
#             return True
#         return False


#     T = int(input())
#     for i in range(T):
#         N, M, K = map(int, input().split())
#         graph = [[0]*M for _ in range(N)]
#         for j in range(K):
#             x, y = map(int, sys.stdin.readline().split())
#             graph[x][y] = 1
        
#         result = 0
#         for i in range(N):
#             for j in range(M):
#                 if dfs(i, j) == True:
#                     result += 1

#         print(result)
    
import sys
from collections import deque
if __name__ == "__main__":
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        graph[x][y] = 0 # 현재 위치 방문 처리

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 탐색 범위가 밭의 범위를 벗어나면
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                # 방문하지 않은 위치면
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
        return


    T = int(input())
    for i in range(T):
        N, M, K = map(int, input().split())
        graph = [[0]*M for _ in range(N)]
        for j in range(K):
            x, y = map(int, sys.stdin.readline().split())
            graph[x][y] = 1
        
        result = 0
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 1:
                    bfs(i, j)
                    result += 1

        print(result)