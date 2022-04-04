import sys
input = sys.stdin.readline
M, N = map(int, input().split())
box = []
# 시작할 토마토 위치 담을 리스트
# 여기서 부터 q 사용해도 됨.
pos = []
visited = [[0]*M for _ in range(N)]
# 우선 각 칸에 모두 임의의 큰 수를 시간값으로 할당
time = [[1e9]*M for _ in range(N)]
for i in range(N):
    box.append(list(map(int, input().split())))
    for k in range(M) :
        if box[i][k] == 1 :
            # 시작 토마토 위치 삽입
            pos.append([i, k])
            # 시작 토마토 칸은 검사에서 제외
            visited[i][k] = 1
            # 시작 시간 0 삽입
            time[i][k] = 0

d = [[0, 1],[0, -1],[1, 0],[-1, 0]]

from collections import deque
q = deque()
for i in range(len(pos)) :
    q.append([pos[i][0], pos[i][1], 0])
while q :
    h, w, tm = q.popleft()
    # if box[h][w] == -1 :
    #     continue
    # time[h][w] = min(time[h][w],tm)
    for i in range(4) :
        next_h = h + d[i][0]
        next_w = w + d[i][1]
        if 0 <= next_h < N and 0 <= next_w < M and visited[next_h][next_w] == 0 and box[next_h][next_w] != -1:
            # " 범위를 벗어나지 않고"  " 검사하지 않은 칸 "이며 " 빈 칸이 아닐 " 경우에만
            q.append([next_h, next_w, tm+1])
            time[next_h][next_w] = tm+1 # 해당 칸까지 익는데 걸린 시간 삽입
            visited[next_h][next_w] = 1 # 검사 처리

mx = -1
for i in range(N):
    for k in range(M) :
        # 단순 빈 칸
        if box[i][k] == -1 : # 밑에 elif 조건문에서 반례 발생할 수도있기 때문에 가장 먼저 조건문 달기
            # 얘도 time에서 1e9 값이기 때문에 잘못하면 elif 에서 걸릴 수 있음
            continue
        elif time[i][k] == 1e9 and box[i][k] == 0 : # time이 업데이트 안된 "안익은 토마토"
            # 하나라도 발견되면
            print(-1)
            sys.exit() # 프로그램 강제 종료
        else : # 익는 시간중 가장 큰 시간
            mx = max(mx, time[i][k])
print(mx)
# print(f"time = {time}")
# print(f"box = {box}")
# print(f"visited = {visited}")
