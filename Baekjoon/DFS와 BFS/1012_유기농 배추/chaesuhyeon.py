# dfs로 풀이 
import sys
sys.setrecursionlimit(10**6) # 재귀 함수 깊이 에러 방지하기 위해 사용
t = int(sys.stdin.readline())

def dfs(x,y):
    if x < 0 or x >= n or y<0 or y>=m :
        return False
    if arr[y][x] == 1:
        arr[y][x] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False



for _ in range(t):
    n, m, k = map(int, sys.stdin.readline().split())
    arr =  [[0]*n for _ in range(m)]
    result = 0 
    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        arr[b][a] = 1


    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                result += 1

    print(result)
