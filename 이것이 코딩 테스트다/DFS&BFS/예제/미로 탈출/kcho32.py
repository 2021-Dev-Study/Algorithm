import sys
from collections import deque


# 상하좌우
drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]
n_row, m_col = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n_row)]


def bfs(row, col):
    queue = deque()
    queue.append((row, col))

    while queue:
        row, col = queue.popleft()

        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]

            if nrow < 0 or nrow >= n_row or ncol < 0 or ncol >= m_col:
                continue
            if maze[nrow][ncol] == 0:
                continue
            if maze[nrow][ncol] == 1:
                maze[nrow][ncol] = maze[row][col] + 1
                queue.append((nrow, ncol))
    return maze[n_row - 1][m_col - 1]

print(bfs(0, 0))