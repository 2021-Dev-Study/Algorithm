'''
7576 토마토 풀이 원리를 활용하면 단순하다.
이것도... 줄일만큼 줄였지만 시간초과네요...
pypy3 패스입니다..!!
'''
import sys
input = sys.stdin.readline
M, N, H = map(int, input().split())
box = []
# 저장될 때부터 모든 토마토가 익어있을 경우 대비
time = [[[0]*M for _ in range(N)]for _ in range(H)]

# 시간 단축을 위해 처음부터 덱에 삽입
from collections import deque
q = deque()
for h in range(H) :
    pan =[]
    for i in range(N):
        pan.append(list(map(int, input().split())))
        for k in range(M) :
            if pan[i][k] == 1 :
                # 시작 토마토 위치 "덱"에 삽입 (층, 세로, 가로)
                q.append([h, i, k, 0])
                # 시작 시간 0 삽입
                time[h][i][k] = 0
    box.append(pan)

d = [[0, 0, 1],[0, 0, -1],[0, 1, 0],[0, -1, 0], [-1, 0, 0],[1, 0, 0]] # [-1, 0, 0] : 아래 / [1,0,0] : 위

while q :
    h, l, w, tm = q.popleft()
    for i in range(6) :
        next_h = h + d[i][0]
        next_l = l + d[i][1]
        next_w = w + d[i][2]
        # 바로 토마토 박스들에 들어있는 안 익은 토마토를 " 익은 토마토 "로 변환해주기 (visited 대용)
        if 0<= next_h < H and 0 <= next_l < N and 0 <= next_w < M and box[next_h][next_l][next_w] == 0 : # box[next_h][next_l][next_w] 조건이 -1(비어있는)의 경우까지 걸러줌.
            q.append([next_h,next_l, next_w, tm+1])
            box[next_h][next_l][next_w] = 1
            time[next_h][next_l][next_w] = tm+1 # 해당 칸까지 익는데 걸린 시간 삽입


mx = -1

# 모두 익을 때까지의 시간 → "안익었다" == "불가능" == 안익은것 또한 하나라도 있으면 안됨.
for h in range(H):
    for i in range(N):
        for k in range(M) :
            if time[h][i][k] == 0 and box[h][i][k] == 0 : # time이 업데이트 안된 "안익은 토마토"
                # 하나라도 발견되면
                print(-1)
                sys.exit() # 프로그램 강제 종료
            else : # 익는 시간중 가장 큰 시간
                mx = max(mx, time[h][i][k])
print(mx)