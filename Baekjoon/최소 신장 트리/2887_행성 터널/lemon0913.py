# 메모리 초과...뜰 것 같았음...ㅎㅎ
# if __name__ == "__main__":
#     def find(parent, x):
#         if parent[x] != x:
#             parent[x] = find(parent, parent[x])
#         return parent[x]
    
#     def union(parent, a, b):
#         a = find(parent, a)
#         b = find(parent, b)
#         if a < b:
#             parent[b] = a
#         else:
#             parent[a] = b
    
#     N = int(input())
#     parent = [0]*(N+1)
#     for i in range(1, N+1):
#         parent[i] = i

#     # 각 행성의 x,y,z 좌표 저장
#     planets = []
#     for i in range(N):
#         x, y, z = map(int, input().split())
#         planets.append((x,y,z))
    
#     edges = []
#     result = 0
#     # 행성간의 비용 모두 구하기
#     for i in range(N):
#         for j in range(i, ):
#             edges.append((min(abs(planets[i][0]-planets[j][0]), abs(planets[i][1]-planets[j][1]), abs(planets[i][2]-planets[j][2])), i+1, j+1))
    
#     edges.sort()

#     for edge in edges:
#         c, a, b = edge
#         if find(parent, a) != find(parent, b):
#             result += c
#             union(parent, a, b)
    
#     print(result)
    


# https://ardentdays.tistory.com/16 그림 참고
# x, y, z 각 좌표별로 정렬했을 때 행성간의 거리를 계산하는 방법
# 이전이 N*N*3번의 연산을 해야 했다면 이 방법은 N*3의 연산을 하는 방법이다
if __name__ == "__main__":
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]
    
    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    N = int(input())
    parent = [0]*(N+1)
    for i in range(1, N+1):
        parent[i] = i

    # 각 행성의 (x,y,z,인덱스)값을 저장 저장
    planets = []
    for i in range(N):
        x, y, z = map(int, input().split())
        planets.append((x,y,z,i+1))
    
    # x, y, z 각 좌표별로 정렬했을 때 행성간의 거리를 계산
    edges = []
    for i in range(3):
        planets.sort(key = lambda x:x[i])

        for j in range(N-1):
            edges.append((abs(planets[j+1][i]-planets[j][i]), planets[j+1][3], planets[j][3]))
    
    edges.sort()

    result = 0
    for edge in edges:
        c, a, b = edge
        if find(parent, a) != find(parent, b):
            result += c
            union(parent, a, b)
    
    print(result)
