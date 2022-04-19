import sys

sys.setrecursionlimit(10 ** 4)
tc = int(input())

for _ in range(tc):
    y, x, cabages = map(int, input().split())
    graph = [[1 for j in range(y)] for i in range(x)]
    answer = 0

    def dfs(row, col):
        if row <= -1 or row >= x or col <= -1 or col >= y:
            return False

        if graph[row][col] == 0:
            graph[row][col] = 1
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            return True

        return False

    for i in range(cabages):
        col, row = map(int, input().split())
        graph[row][col] = 0

    for i in range(x):
        for j in range(y):
            if dfs(i, j) == True:
                answer += 1
    
    print(answer)

