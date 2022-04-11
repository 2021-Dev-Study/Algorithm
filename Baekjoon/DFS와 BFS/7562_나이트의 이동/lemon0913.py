import sys
from collections import deque
if __name__ == "__main__":
    
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    def bfs(a, b, na, nb, l):
        queue = deque()
        queue.append((a,b))

        while queue:
            x, y = queue.popleft()

            if x == na and y == nb:
                print(visited[x][y])
                break

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= l or ny >= l:
                    continue
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
    
    T = int(input())
    for _ in range(T):
        l = int(input())
        a, b = map(int, sys.stdin.readline().split())
        na, nb = map(int, sys.stdin.readline().split())
        visited = [[0]*l for _ in range(l)]
        bfs(a, b, na, nb, l)