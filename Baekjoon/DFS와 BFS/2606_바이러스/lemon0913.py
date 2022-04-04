import sys
if __name__ == "__main__":
    N = int(input())
    c = int(input())
    connect = [[]*N for _ in range(N+1)]
    for i in range(c):
        a, b = map(int, sys.stdin.readline().split())
        connect[a].append(b)
        connect[b].append(a)
    
    cnt = 0
    visited = [False] * (N+1)

    def dfs(v):
        global cnt
        # 현재 노드를 방문 처리
        visited[v] = True
        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for i in connect[v]:
            if not visited[i]:
                dfs(i)
                cnt += 1

    dfs(1)
    print(cnt)
