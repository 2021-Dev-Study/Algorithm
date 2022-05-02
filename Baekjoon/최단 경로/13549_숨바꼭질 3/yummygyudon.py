import sys
input = sys.stdin.readline

N, K = map(int, input().split())

import heapq
q = []
heapq.heappush(q, [0, N])
dis = [1e9]*100001
dis[N] = 0

while q:
    t, pos = heapq.heappop(q)
    if pos == K :
        print(dis[pos])
        break
    for m in [pos*2, pos+1, pos-1] :
        if 0 <= m < 100001 and dis[m] == 1e9:
            if m == pos*2 :
                dis[m] = t
                heapq.heappush(q,[t, m])
            else :
                dis[m] = t+1
                heapq.heappush(q,[t+1, m])