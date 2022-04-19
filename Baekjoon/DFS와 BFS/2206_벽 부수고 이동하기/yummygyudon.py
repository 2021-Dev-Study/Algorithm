import sys
from collections import deque
input = sys.stdin.readline
H, W =  map(int, input().split())
# 지도
m = [list(map(int, list(input().rstrip()))) for _ in range(H)]

# print(check)
# print(m)
d = [[0,1], [0,-1], [1,0], [-1,0]]

def bfs() :
    q = deque()
    q.append([0, 0, 1]) # (1,1) 좌표 시작 & 벽 부술 수 있는 횟수
    # 끝나는 칸도 포함해서 세야함
    dis = [[[0] * 2 for _ in range(W)] for _ in range(H)]
    dis[0][0][1] = 1
    while q :
        x, y, crack = q.popleft()
        if x == W-1 and y == H-1 :
            return dis[y][x][crack]
        for i in range(4):
            nx = x+d[i][0]
            ny = y+d[i][1]
            if 0 <= nx < W and 0 <= ny < H :
                if m[ny][nx] == 1 and crack == 1  :#and dis[ny][nx][crack-1] == 0
                    dis[ny][nx][0] = dis[y][x][1] + 1
                    q.append([nx, ny, 0])
                elif m[ny][nx] == 0   and dis[ny][nx][crack] == 0 : # 이거 꼭 빼야함 ( and crack == 0) : 벽을 안부쉈어도  그냥 갈 수 있기 때문
                    dis[ny][nx][crack] = dis[y][x][crack] + 1
                    q.append([nx, ny, crack])
    return -1
print(bfs())

# from collections import deque
# q = deque()
# q.append([0, 0, 1]) # (1,1) 좌표 시작 & 벽 부술 수 있는 횟수
# # 끝나는 칸도 포함해서 세야함
# dis[0][0][1] = 1
#
# """ 시간 초과 """
# while q :
#     x, y, crack = q.popleft()
#     if x == W-1 and y == H-1 :
#         print(dis[y][x][crack])
#         sys.exit()
#     for i in range(4):
#         nx = x+d[i][0]
#         ny = y+d[i][1]
#         # 부술 기회 없는데 벽이 있는 경우 "불가능"
#         if 0 <= nx < W and 0 <= ny < H :
#             # 부술 기회 남은 경우 & 벽이 있을 경우 (벽 부술 경우)
#             if m[ny][nx] == 1 and crack == 1  :#and dis[ny][nx][crack-1] == 0
#                 dis[ny][nx][0] = dis[y][x][1] + 1
#                 q.append([nx, ny, 0])
#             # 기회는 없지만 다행히 벽이 아닌경우 (그냥 통과
#             elif m[ny][nx] == 0 and crack == 0  and dis[ny][nx][crack] == 0 :
#                 dis[ny][nx][crack] = dis[y][x][crack] + 1
#                 q.append([nx, ny, crack])
#
#
#
# print(-1)
