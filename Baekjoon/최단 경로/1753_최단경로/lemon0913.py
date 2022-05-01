import sys
input = sys.stdin.readline
INF = int(1e9)
import heapq

if __name__ == "__main__":
    V, E = map(int, input().split())
    K = int(input())
    graph = [[] for i in range(V+1)]
    for i in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v,w))
    
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF]*(V+1)

    # 다익스트라 알고리즘 수행
    def dijkstra(start):
        q = []
        # 시작 노드로 가기 위한 최단 경로를 0으로 설정하고 큐에 삽입
        distance[start] = 0
        heapq.heappush(q, (0,start))

        while q:
            # 가장 거리가 짧은 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(q)
            # 만약 처리된 적 있는 노드라면 무시하기
            if distance[now] < dist:
                continue
            # 현재 노드와 연결된 다른 인접한 노드들을 확인하기
            for x in graph[now]:
                cost = dist + x[1]
                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 짧은 경우 갱신하기
                if cost < distance[x[0]]:
                    distance[x[0]] = cost
                    heapq.heappush(q, (cost, x[0]))
    
    # 다익스트라 알고리즘 수행
    dijkstra(K)

    for i in range(1, V+1):
        if distance[i] == INF:
            print('INF')
        else:
            print(distance[i])



