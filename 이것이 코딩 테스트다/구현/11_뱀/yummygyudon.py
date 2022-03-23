# # 보드 크기 - 사과 개수 - 사과 위치 - 방향변환 횟수 - (시작시간 X초후, 90도 회전 방향)
#
# # 사과 없으면 몸길이 줄이기 ( visited로 관리? )
# # 범위 벗어나거나 몸과 부딪히면  게임종료
#
# # 처음 : (0,0)위치에 오른쪽방향으로

# 끝난뒤에 방향바뀌는 점 유의
def direct_rotate(now_d, direct) :
    if direct =="L" :
        now_d = now_d-1
        if now_d == -1 :
            now_d = 3
    else :
        now_d = now_d + 1
        if now_d == 4 :
            now_d = 0
    return now_d

N = int(input())
m = [[0]*(N+1) for _ in range(N+1)]
visited = [[0]*(N+1) for _ in range(N+1)]

K = int(input())
# pos_apple = []
for _ in range(K) :
    h, w = map(int,input().split())
    m[h][w] = 1

L = int(input())
change_d = dict()
for _ in range(L) :
    x, c = input().split()
    change_d[int(x)] = c
#
# print(change_d)
# 첫번째는 오른쪽 & 순서는 오른쪽으로 90도 돌아가는
d = [[0,1], [1,0], [0,-1], [-1,0]] # 오른쪽, 아래, 왼쪽, 위쪽

end_time = 0

from collections import deque
q = deque()
# body = deque([1,1])
q.append([ [[1,1]] ,0]) # 위치 & 방향
visited[1][1] = 1
while q :
    body_ls, dir = q.popleft()
    # print(body_ls)
    # 머리 부분
    now_y = body_ls[-1][0] + d[dir][0]
    now_x = body_ls[-1][1] + d[dir][1]
    # 머리가 m 범위 내이면서 꼬리가 있지 않은 곳
    if 1 <= now_y <= N and 1<= now_x <= N and visited[now_y][now_x] == 0 :
    # 사과가 있을 때
        if m[now_y][now_x] == 1:
            # 머리만 늘리고 꼬리는 냅두기
            body_ls.append([now_y, now_x]) # 머리만 추가
            m[now_y][now_x] = 0 # 사과 먹은거 없애기
            visited[now_y][now_x] = 1 # 머리 방문 체크
        else :
            # 머리가 늘어난 것을 추가 & 꼬리 줄이기
            body_ls.append([now_y, now_x]) # 머리 추가
            visited[now_y][now_x] = 1 # 머리 방문 체크
            tail_y, tail_x = body_ls.pop(0) # 꼬리 삭제
            visited[tail_y][tail_x] = 0 # 꼬리 부분 다시 방문 0으로 초기화

        end_time += 1 # 초 경과 누적
        if end_time in change_d: # 끝난 뒤 방향 바뀌는 것
            dir = direct_rotate(dir, change_d[end_time])
        q.append([body_ls, dir])
    else :
        end_time += 1
        break

print(end_time)

