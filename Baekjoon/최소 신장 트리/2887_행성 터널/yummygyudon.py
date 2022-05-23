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
N = int(input())
pos = []
parent = [i for i in range(N)]
dis = []
for i in range(N) :
    x, y, z = map(int, input().split())
    pos.append([x, y, z, i])# i를 추가 -> 어느 행성 좌표인지


"""
여기서는 검색을 해봤습니다. 

단 3가지 좌표 경로에 대해 최소 경로를 구하기 때문에
한 가지 좌표당 행성개수만큼만 반복하면 된다.

for i in range(N-1) & for k in range(i+1,N) -> N-1*N/2 번이나 반복된 것을
단 3*N-1 만 반복하게 됨
"""
# 각 좌표별 경로 비용 계산
for i in range(3) : # 행성의 개수가 몇개든 단 x,y,z 3가지 경우의 거리만 구하면 됨
    pos.sort(key=lambda x:x[i]) 
    base_planet = pos[0][3] # 최소 값을 가진 행성 시작
    for k in range(1,N) : # 시작 행성 제외 
        curr_planet = pos[k][3]
        # 오름차순 경로 비용 -> 순서대로 비용 삽입( 삽입도 자동으로 오름차순 정렬되서 삽입되는 모양 ) 
        dis.append([abs(pos[k][i]-pos[k-1][i]), base_planet, curr_planet])
        base_planet = curr_planet # 최소 경로인 순서대로 한 행성씩 좌표별 거리 구하기

# 3가지 좌표의 각 경로 비용을 합친  ""전체 경로 비용"" 중에서도
# 가장 최소 비용인 값들을 순서대로 뽑으면서 최소신장트리 만들기
"""
즉, 먼저 각 좌표(x, y, z)별로 최소 경로들을 구하고
이후, 이 전체 경로의 경우들을 합친 상태에서
다시 최소 거리를 가진 경로들을 우선적으로 먼저 꺼내면서
최소 신장 트리를 만드는 것
"""
dis.sort(key=lambda x : x[0])# 거리 기준으로 전체 경로 sorting

ans = 0

for d in dis :
    cost, e1, e2 = d[0], d[1], d[2]
    if find_parent(parent, e1) != find_parent(parent, e2) :
        union_parent(parent, e1, e2)
        ans += cost

print(ans)