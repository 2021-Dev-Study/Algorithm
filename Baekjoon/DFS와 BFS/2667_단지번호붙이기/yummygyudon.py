import sys
input = sys.stdin.readline
N = int(input())
Map = []
# checked =[]
for _ in range(N) :
    Map.append(list(map(int, input().rstrip())))
    # checked.append([False]*N)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x,y) :
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if Map[x][y] == 1 :
        global house_cnt
        Map[x][y] = 0
        house_cnt += 1
        # for i in range(4) :
        #     nx= x+dx[i]
        #     ny= y+dy[i]
        #     dfs(nx,ny)
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

cnt = 0
Each = []
house_cnt = 0
for i in range(N):
    for k in range(N) :
        if dfs(i,k) :
            Each.append(house_cnt)
            cnt+=1
            house_cnt = 0
print(cnt)
Each.sort()
for i in Each :
    print(i)