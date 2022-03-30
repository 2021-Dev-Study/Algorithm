import sys
input = sys.stdin.readline
TC = int(input())

for _ in range(TC) :
    W, H, C = map(int, input().split())
    field = [[0]*W for _ in range(H)]
    for _ in range(C) :
        x, y = map(int, input().split())
        field[y][x] = 1

    def dfs(x, y) :
        if x < 0 or x >= H or y < 0 or y >= W :
            return False
        if field[x][y] == 1 :
            field[x][y] = 0
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            return True
        return False

    bugs = 0
    for i in range(H) :
        for k in range(W) :
            if dfs(i, k) :
                bugs+=1

    print(bugs)