# 최소라는 말이 있어서 bfs로 풀 생각함 - 이코테 미로찾기랑 비슷한듯

import sys
from collections import deque
m,n = map(int, sys.stdin.readline().split())

arr=[]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0
queue = deque([])

for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
    for j in range(m):
        if arr[i][j] == 1: # 토마토 위치 넣어주기
            queue.append([i, j])


def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]            
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0: # 범위 안벗어나는지 확인 & 0일경우
                arr[nx][ny] = arr[x][y] + 1 # 누적 합 구해줌
                queue.append([nx, ny])

bfs() # 함수 실행해서 누적합들 다 구해줌
for i in arr: # arr에서 한행씩 뽑아서 (i)
    for j in i: # i에서 낱개로 뽑았을 때
        if j == 0: # 0이 하나라도 나오면 다 익히지 못했으므로 -1을 출력
            print(-1)
            exit(0) # 바로 종료 시킴 
    cnt = max(cnt, max(i)) # 정확한 마지막 위치를 모르기 때문에 한행 씩 뽑아서 최댓값이 있으면 그것으로 바꿔주기

print(cnt -1) # 1은 포함시키면 안되기 때문에 1빼줌(1부터 시작했기 때문에)   


