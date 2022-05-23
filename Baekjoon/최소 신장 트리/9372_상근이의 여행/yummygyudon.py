def dfs(point, cnt) :
    visited[point] = True
    for p in graph[point] :
        if visited[p] == False :
            cnt = dfs(p,cnt+1)
    return cnt
    
import sys
input = sys.stdin.readline
TC = int(input())
for _ in range(TC) :
    N, M = map(int, input().split())  
    graph = [[] for _ in range(N+1)]

    for _ in range(M) :
        s,a = map(int, input().split())
        graph[s].append(a)
        graph[a].append(s)

    visited = [False]*(N+1)
    print(dfs(1,0))