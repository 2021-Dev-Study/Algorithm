import sys
# sys.setrecursionlimit(10**7)
input = sys.stdin.readline
''' dfs 도전2'''
def distance(dis : list) :
    for i in range(len(house)) :
        h_y, h_x = house[i]
        for k in range(len(store)) :
            if checked[k]:
                s_y, s_x = store[k]
                d= abs(h_y - s_y) + abs(h_x - s_x)
                dis[i] = min(d, dis[i])
    return sum(dis)

def combi_store(store_idx, count_mem) :
    global result
    if count_mem == M :
        dis = [1e9]*len(house)
        result = min(distance(dis), result)
        return

    for i in range(store_idx, len(store)) :
        if checked[i] :
            continue
        checked[i] = 1
        combi_store(i + 1, count_mem+1 )
        checked[i] = 0 #뒤에 남아있는 가게들 체크를 다음 순서를 위해 초기화

N, M = map(int, input().split())
m = []
house, store = [], []
for i in range(N):
    m.append(list(map(int, input().split())))
    for k in range(N) :
        if m[i][k] == 1 :
            house.append([i, k])
        elif m[i][k] == 2 :
            store.append([i, k])
# 각 집 ~ 가장 가까운 치킨집 거리 담을 리스트
checked = [0]*len(store)
result = 1e9
combi_store(0,0)

print(result)

''' bfs 도전 '''
# m = []
# for _ in range(N):
#     m.append(list(map(int, input().split())))
# toEachHouse = []
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# from collections import deque
# def bfs(x, y) :
#     q= deque()
#     visited =[[0]*N for _ in range(N)]
#     dis = 0
#     q.append([x, y, 0, False])
#     visited[y][x] = 1
#     while q :
#         now_x, now_y, count, isOne = q.popleft()
#         print(now_x, now_y, count)
#         # if m[now_y][now_x] == 1  :
#         #     dis = count
#         #     break
#         if isOne:
#             dis += count
#             continue
#         for i in range(4):
#             nx = now_x + dx[i]
#             ny = now_y + dy[i]
#             if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == 0 :
#                 if m[ny][nx] == 0 :
#                     visited[ny][nx] = 1
#                     q.append([nx,ny,count+1,False])
#                 elif m[ny][nx] ==1 :
#                     q.append([nx, ny, count + 1, True])
#
#     return dis
#
# for i in range(N) :
#     for k in range(N):
#         if m[i][k] == 2 :
#             # dis = []
#             # count_house(k, i, 0)
#             toEachHouse.append(bfs(k, i))


''' dfs 도전1 (실패) '''
#m = []
# for _ in range(N):
#     m.append(list(map(int, input().split())))
#
# toEachHouse = []
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# def count_house(x, y, cnt) :
#     if m[y][x] == 1 :
#         dis.append(cnt)
#         return True
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < N and 0 <= ny <N :
#             if m[ny][nx] == 0 :
#                 count_house(nx, ny, cnt+1)
#     return True
#
# for i in range(N) :
#     for k in range(N):
#         if m[i][k] == 2 :
#             dis = []
#             count_house(k, i, 0)


