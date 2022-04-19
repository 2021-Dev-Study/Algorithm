# 사이클 여부 문제

import sys
from collections import deque
input = sys.stdin.readline
TC = int(input())
for _ in range(TC) :
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 그룹의 가능성 1 ~ V
    group=[0]*(V+1)
    g = 1 # 1번 그룹부터 시작
    bipartite = True
    q = deque()
    for n in range(1,V+1) :
        if group[n] == 0 : # 그룹 지정이 안된 상태
            q.append(n)
            group[n] = g
            while q :
                v = q.popleft()
                for c in graph[v] :
                    if group[c] == 0:
                        q.append(c)
                        group[c] = 20000 + group[v] # 정점의 최대범위 20000 -> 임의의 별도 그룹으로 분리
                    elif group[c] == group[v] : # 사이클 발생
                        bipartite = False
                        break
        # 시간 효율 위해 n 마다 검사
        if not bipartite :
            break
    print("YES" if bipartite else "NO")