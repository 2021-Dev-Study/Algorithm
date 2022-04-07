import sys
input = sys.stdin.readline

TC = int(input())
d = [(-1,-2), (-2,-1), (-2,1), (-1,2), (1, 2), (2, 1), (2, -1), (1,-2)]


from collections import deque
for _ in range(TC):
    I = int(input())
    nx, ny = map(int, input().split())
    want_x, want_y = map(int,input().split())
    visited = [[0]*I for _ in range(I)]
    move_cnt = 0
    q = deque()
    q.append([nx,ny, move_cnt])
    visited[ny][nx] = 1
    while True :
        x, y, cnt = q.popleft()
        if x == want_x and y == want_y :
            print(cnt)
            break
        for dy,dx in d :
            next_x = x + dx
            next_y = y + dy
            if 0<=next_x<I and 0<=next_y<I and visited[next_y][next_x] == 0 :
                visited[next_y][next_x] = 1
                q.append([next_x, next_y, cnt+1])

