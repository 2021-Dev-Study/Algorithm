import sys
input = sys.stdin.readline

N, K =  map(int, input().split())

''' 런타임 에러 때문에 수정한 답안 '''
# visited의 기능과 cnt값을 저장하는 기능을 동시에
# 0보다 크면 일단 들렸었던 값 & 최소 방문횟수 저장
counting = [0]*100001
limit = 100000

from collections import deque
q = deque()
q.append(N)


while q:
    now= q.popleft()
    if now == K :
        print(counting[now])
        break
    if 0 <= now-1 <= limit and counting[now-1] == 0:
        counting[now-1] = counting[now]+1
        q.append(now-1)
    if 0 <= now+1 <= limit and counting[now+1] == 0 :
        counting[now+1] = counting[now]+1
        q.append(now+1)
    if 0 <= now*2 <= limit and counting[now*2] == 0 :
        counting[now*2] = counting[now]+1
        q.append(now*2)

''' 시간/메모리 제한 없다면 가능 '''
# import sys
# input = sys.stdin.readline
#
# N, K =  map(int, input().split())
#
# visited = [0]*100001
#
# from collections import deque
# q = deque()
# q.append([N,0])
# visited[N] = 1
#
# while q:
#     now, cnt = q.popleft()
#     if now == K :
#         print(cnt)
#         break
#     if now < 0 or now > 100000 :
#         continue
#     if now-1 >= 0 and visited[now-1] == 0:
#         visited[now-1] = 1
#         q.append([now-1, cnt+1])
#     if now+1 <= 1000000 and visited[now+1] == 0 :
#         visited[now+1] = 1
#         q.append([now+1, cnt+1])
#     if now*2 <= 1000000 and visited[now*2] == 0 :
#         visited[now*2] = 1
#         q.append([now*2, cnt+1])