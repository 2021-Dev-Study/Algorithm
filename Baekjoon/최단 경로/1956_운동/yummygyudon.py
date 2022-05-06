import sys
import heapq # 짧은 것부터 찾기 위해 힙쓰기
input = sys.stdin.readline
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
dist = [[1e9]*(V+1) for _ in range(V+1)] # 거리 테이블

q = []
for _ in range(E) :
    a, b, c = map(int, input().split())
    graph[a].append([c, b]) # heap에서 쓰기위해서 비용을 앞으로
    dist[a][b] = c
    heapq.heappush(q, [c, a, b]) # a 는 시작위치 귀환을 위해 필요한 시작위치 기본값

while(q) :
    d, start, arrived = heapq.heappop(q)
    if start == arrived :
        print(d)
        sys.exit(0)
    if dist[start][arrived] < d :
        continue

    for next_d, next_a in graph[arrived] :
        nd = d+next_d # 다음 위치까지 갔을 때의 거리 총합
        if nd < dist[start][next_a] : # 거리 테이블에서
            '''
            start -> arrived(현재) -> next_a(다음) 거리가
            start -> next_a(다음) _ 기존에 저장되어 있던 직행거리보다 가까우면
            위 경유 거리값으로 최단 거리 갱신신
           '''
            dist[start][next_a] = nd
            heapq.heappush(q, [nd, start, next_a])


print(-1)