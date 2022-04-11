from collections import deque
if __name__== "__main__":
    N, K = map(int, input().split())

    
    def bfs(start):
        queue = deque()
        queue.append(start)

        while queue:
            v = queue.popleft()
            if v == K:
                print(visited[v])
                break
            for nv in (v-1, v+1, 2*v):
                if 0 <= nv <= MAX and not visited[nv]:
                    visited[nv] = visited[v] + 1
                    queue.append(nv)

    MAX = 10 ** 5
    visited = [0] * (MAX+1)

    bfs(N)


