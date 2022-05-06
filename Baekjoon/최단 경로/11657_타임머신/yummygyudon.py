# 음의 순환 발생 -> -1 출력

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 1번 도시 출발

for _ in range(M) :
    a,b,c = map(int, input().split())
    graph[a].append([b,c])

able = True
dis = [1e9] * (N+1)
dis[1] = 0
# N-1번 만큼만 먼저 반복
for _ in range(N-1) :
    for s in range(1, N+1) :
        for arrv, cost in graph[s] :
            # 1 부터 시작해서 (dis[1] = 0)
            # 모든 정점을 모두 검사하는데
            # 1e9가 아닌 즉,  1에서 출발하는게 조건이기 때문에
            # 만약 dis[s]가 1e9 라는 것은 애초에 1에서 출발이 안되었다는 걸 의미하기 때문에
            # 반복문마다 dis[s] != 1e9 를 설정해줘야한다.
            if dis[s] != 1e9 and dis[arrv] > dis[s] + cost :
                dis[arrv] = dis[s] + cost

# N번째 반복 때
# 음수 사이클 체크  -> N번째 반복 때에도 거리 값이 갱신되는것 --> " 음수 순환이 발생 "
for s in range(1, N+1) :
    for arrv, cost in graph[s] :
        if dis[s] != 1e9 and  dis[arrv] > dis[s] + cost : # 값이 또 더 줄어듦
            able = False

if able :
    for i in range(2,N+1) :
        # 1e9이다 --> 해당 도시로 가는 경로가 없다.
        print(dis[i] if dis[i] < 1e9 else -1)
else :
    print(-1)