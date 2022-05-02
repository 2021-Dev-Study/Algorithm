import sys
input = sys.stdin.readline
C = int(input())
B = int(input())

graph = [[1e9] * (C + 1) for _ in range(C + 1)]
for i in range(1, C+1) :
    for k in range(1, C+1) :
        if i == k :
            graph[i][k] = 0

for _ in range(B) :
    s_city, a_city, cost = map(int, input().split())
    # s_city(출발) 에서 a_city(도착) 노선 버스의 비용 등록
    graph[s_city][a_city] = min(cost, graph[s_city][a_city]) # " 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다." 라는 조건 -> min()

for w_point in range(1, C+1) : # 경유지
    for s in range(1, C+1) : # 시작 도시
        for a in range(1, C+1) : # 도착 도시
            # 최저 비용 설정
            # s -> a 직통 방법이 없다면 1e9가 될 것 -> 경유하는 경우의 비용 합이 들어가게됨
            # 갈 수 있는 방법이 없다 -> min(1e9, 1e9 + x ) ->1e9 라는 값
            graph[s][a] = min(graph[s][a], graph[s][w_point]+graph[w_point][a])

for a in range(1, C+1) :
    for b in range(1, C+1) :
        if graph[a][b] == 1e9 :
            print(0, end =" ")
        else :
            print(graph[a][b], end = " ")
    print()