import sys

def dfs(cols, rows):
    if cols <= -1 or cols >= m or rows <= -1 or rows >= n:
        # 범위가 벗어날 경우, False 리턴
        return False
    
    if graph[rows][cols] == 0:
        # 방문처리
        graph[rows][cols] = 1
        # 상하좌우 방문 재귀 -> 모든 연결 방문
        dfs(cols + 1, rows)
        dfs(cols - 1, rows)
        dfs(cols, rows + 1)
        dfs(cols, rows - 1)
        return True
    
    return False
        

# n: rows 행, m: cols 열
n, m = map(int, input().split())
answer = 0
graph = []
for i in range(n):
    graph.append(list(map(int, list(sys.stdin.readline().rstrip()))))


for rows in range(n):
    for cols in range(m):
        if dfs(cols, rows) == True:
            answer += 1

print(answer)