H, W = map(int, input().split())
m = []
for _ in range(H) :
    m.append(list(input()))
# N,M 위치는 N-1,M-1 일 때임

visited = [[0]*W for _ in range(H)]

from collections import deque

d = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs() :
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    while q :
        y, x = q.popleft()
        # if m[y][x] =='0' :
        #     continue
        for dy, dx in d :
            ny = y + dy
            nx = x + dx
            if 0 <= ny < H and 0 <= nx < W and visited[ny][nx] == 0 and m[ny][nx]=='1' :
                q.append([ny,nx])
                visited[ny][nx] = visited[y][x] + 1

bfs()
print(visited[H-1][W-1])
