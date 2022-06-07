def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b : 
        parent[b] = a
    else :
        parent[a] = b

    
import sys
input = sys.stdin.readline
"""
모든 지점의 부모(루트)는 한 지점이여야 함 -> union find 사용
"""
V, E = map(int, input().split())  
parent = [0] * (V+1)
# 각자의 값으로 부모 설정
for i in range(1, V+1) :
    parent[i] = i

edges = []
for _ in range(E) :
    a, b, c = map(int, input().split())
    # 비용을 맨 앞에 -> sort() : key 속성 설정 안해주면 자동 맨 앞자리값 기준으로 정렬
    edges.append([c,a,b])
edges.sort()

ans = 0
# 비용이 가장 적은 순서먼저 & 정점 index 순
for e in edges :
    cost, p1, p2 = e[0], e[1], e[2]
    # 두 지점의 부모가 같지 않은 경우
    # 하나의 정점으로 동일하지 않다 -> 아직 union을 안했다
    if find_parent(parent, p1) != find_parent(parent, p2) :
        union_parent(parent, p1, p2)
        # 거리순으로 사이클 돌려보니까 union 시켜줄 때마다 거리 더해주기
        ans += cost

print(ans)