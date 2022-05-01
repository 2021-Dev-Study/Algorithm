# bfs 풀이..??
# import sys
# from collections import deque
# if __name__ == "__main__":
#     N, K = map(int, input().split())
#     q = deque()
#     q.append(N)

#     visited = [-1 for _ in range(100001)]

#     # 수빈이의 현재 위치는 방문 처리
#     visited[N] = 0

#     while q:
#         x = q.popleft()

#         # 수빈이가 동생과 만나면 탐색 끝
#         if x == K:
#             print(visited[x])
#             break
#         # x-1이 아직 방문하지 않은 위치인 경우 큐에 넣기
#         if 0 <= x-1 <= 100000 and visited[x-1] == -1:
#             visited[x-1] = visited[x]+1
#             q.append(x-1)
#         # x+1이 아직 방문하지 않은 위치인 경우 큐에 넣기
#         if 0 <= x+1 <= 100000 and visited[x+1] == -1:
#             visited[x+1] = visited[x] + 1
#             q.append(x+1)
#         # 2*x가 아직 방문하지 않은 위치인 경우 큐에 넣기
#         if 0 <= 2*x <= 100000 and visited[2*x] == -1:
#             visited[x*2]=visited[x]
#             q.appendleft(x*2)


# 다익스트라로 푼다고 푼건데 맞는건지는 모르겠다...
# 답은 맞게 나옴
import heapq
INF = int(1e9)

if __name__ == "__main__":
    N, K = map(int, input().split())
    visited = [INF]*100001

    # 다익스트라 알고리즘 수행
    q = []
    visited[N] = 0
    heapq.heappush(q, (0, N))
    while q:
        dist, now = heapq.heappop(q)
        if visited[now] < dist:
            continue
        
        # now+1, now-1, now*2를 q에 넣기!
        if 0 <= now+1 <= 100000:
            cost = dist + 1
            if cost < visited[now+1]:
                visited[now+1] = cost
                heapq.heappush(q, (cost, now+1))

        if 0 <= now-1 <= 100000:
            cost = dist + 1
            if cost < visited[now-1]:
                visited[now-1] = cost
                heapq.heappush(q, (cost, now-1))

        if 0 <= now*2 <= 100000:
            cost = dist
            if cost < visited[now*2]:
                visited[now*2] = cost
                heapq.heappush(q, (cost, now*2))

    print(visited[K])