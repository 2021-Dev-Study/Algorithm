import sys
input = sys.stdin.readline
INF = int(1e9)

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = [[INF]*(n+1) for _ in range(n+1)]
    # 자기 자신으로 이동하는 경우는 0으로
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a==b:
                graph[a][b] = 0
    
    for i in range(m):
        a, b, c = map(int, input().split())
        if graph[a][b] > c:
            graph[a][b] = c
    
    
    
    # 플로이드 워셜 알고리즘 수행
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])
    
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] == INF:
                print(0, end=' ')
            else:
                print(graph[a][b], end = ' ')
        print()

    

