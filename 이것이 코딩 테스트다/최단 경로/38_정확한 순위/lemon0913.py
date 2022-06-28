# 플로이드 워셜 알고리즘
import sys
input = sys.stdin.readline
INF = int(1e9)

if __name__ == "__main__":
    # 일단 플로이드 워셜 알고리즘 수행
    N, M = map(int, input().split())
    graph = [[INF]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a][b] = 1
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                graph[i][j] = 0

    for k in range(1, N+1):
        for a in range(1, N+1):
            for b in range(1, N+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
    
    
    # graph의 모든 노드에 대해 다른 노드와 서로 도달이 가능한지 체크
    result = 0
    for i in range(1, N+1):
        cnt = 0
        for j in range(1, N+1):
            if graph[i][j] != INF or graph[j][i] != INF:
                cnt += 1
        if cnt == N:
            result += 1
    print(result)

    