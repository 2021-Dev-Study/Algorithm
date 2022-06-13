if __name__ == "__main__":
    T = int(input())
    for _ in range(T):

        n, m = map(int, input().split())
        tmp = list(map(int, input().split()))
        graph = []
        for i in range(n):
            graph.append(tmp[i*4:i*4+4])
        
        for i in range(1, m):
            for j in range(n):
                if j-1 >=0 and j+1 < n:
                    graph[j][i] = graph[j][i] + max(graph[j-1][i-1], graph[j][i-1], graph[j+1][i-1])
                elif j-1 >= 0 and j+1 >=n:
                    graph[j][i] = graph[j][i] + max(graph[j-1][i-1], graph[j][i-1])
                elif j-1 < 0 and j+1 < n:
                    graph[j][i] = graph[j][i] + max(graph[j][i-1], graph[j+1][i-1])
                else:
                    graph[j][i] = graph[j][i] + graph[j][i-1]
        
        t = graph[0][m-1]
        for i in range(1,n):
            t = max(t, graph[i][m-1])
        print(t)
