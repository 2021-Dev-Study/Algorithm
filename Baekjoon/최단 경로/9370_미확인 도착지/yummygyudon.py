import sys, heapq as heap

input = sys.stdin.readline
"""
도저히 저 점선을 어떻게 처리해야할지 모르겠어서
검색을 통한 참고를 했습니다..!!
"""


def dijkstra(points, start, graph):
    dis = [1e9] * (points + 1)
    dis[start] = 0

    q = []
    heap.heappush(q, [0, start])
    while q:
        cost, now = heap.heappop(q)
        if dis[now] < cost:
            continue

        for v in graph[now]:
            n_cost = dis[now] + v[0]
            n_point = v[1]

            if n_cost < dis[n_point]:
                dis[n_point] = n_cost
                heap.heappush(q, [n_cost, n_point])

    return dis


TC = int(input())
for _ in range(TC):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        # 냄새를 맡았다 == 무조건 지나가야 한다.
        # 다익스트라를 통해 도출된 "도착지의 dis값"을 확인해봤을 때,
        # 만약 실수형이 아니라면 "안지나갔다는 것" -> 해당 도착지는 진짜 도착지가 아니다!
        # 적어도 1개의 후보로 이동하는 최단 경로의 일부이기 때문에 둘다 안지나간 결과가 나올 수 없음
        a, b, d = map(int, input().split())
        if (a == g and b == h) or (a == h and b == g):
            d -= 0.1
        graph[a].append([d, b])
        graph[b].append([d, a])

    arrived = []
    for _ in range(t):
        arrived.append(int(input()))
    # 여기서 미리 정렬해서 나중에 for문으로 오름차순 출력
    arrived.sort()
    dijk_dis = dijkstra(n, s, graph)
    for a in arrived:
        if type(dijk_dis[a]) == float and dijk_dis[a] != 1e9:
            print(a, end=" ")
