import sys
from collections import deque

input = sys.stdin.readline
sb, bro = map(int, input().split())
INF = int(1e9)
dist = [INF for _ in range(100001)]
visited = [False for _ in range(100001)]

q = deque([])
q.append(sb)
visited[sb] = True
dist[sb] = 0

while q:
    now = q.popleft()
    if now * 2 < 100001 and not visited[now * 2]:
        dist[now * 2] = dist[now]
        visited[now * 2] = True
        q.appendleft(now * 2)
    
    if now + 1 < 100001 and not visited[now + 1]:
        dist[now + 1] = dist[now] + 1
        visited[now + 1] = True
        q.append(now + 1)
    
    if now - 1 >= 0 and not visited[now - 1]:
        dist[now - 1] = dist[now] + 1
        visited[now - 1] = True
        q.append(now - 1)
    

print(dist[bro])

# import heapq, sys
# input = sys.stdin.readline
# INF = int(1e9)

# sb, bro = map(int, input().split())

