import sys
input = sys.stdin.readline
INF = int(1e9)
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = [[INF]*(n+1) for _ in range(n+1)]

    for i in range(m):
        a, b, c = map(int, input().split())
        if graph[a][b] > c: # 시작도시와 도착도시를 연결하는 노선은 하나가 아닐 수 있다
            graph[a][b] = c

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0

    
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
    

    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] == INF:
                print(0, end=' ')
            else:
                print(graph[a][b], end = ' ')
        print()