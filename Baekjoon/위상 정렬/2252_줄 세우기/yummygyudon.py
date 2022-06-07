import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degree = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    degree[b] += 1
    graph[a].append(b)

q = deque()
# 진입 차수 없는 수들 -> 먼저 앞에 정렬 
for i in range(1, N+1):
    if degree[i] == 0 :
        q.append(i)

while q :
    now = q.popleft()
    print(now, end=" ")
    for n in graph[now] :
        degree[n] -= 1
    # -1 했더니 차수가 없어지면 해당 노드도
    # 앞에 위치할 순서가 됨. -> q 삽입
        if degree[n] == 0 :
            q.append(n)