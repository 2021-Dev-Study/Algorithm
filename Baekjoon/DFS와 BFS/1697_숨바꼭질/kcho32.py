from collections import deque

su, si = map(int, input().split())
graph = [0 for i in range(2 * max(su, si))]
dest_flag = False
dy = [-1, 1] #좌우
queue = deque([su])


def bfs():
    while queue:
        y = queue.popleft()
        global dest_flag

        if dest_flag:
            break

        for i in range(2):
            dy1 = y + dy[i]
            dy2 = y * 2
            print(dy1, dy2)
            if dy1 <= -1 or dy1 >= len(graph):
                continue
            
            if graph[dy1] == 0:
                graph[dy1] = graph[y] + 1
                queue.append(dy1)

            if dy2 <= -1 or dy2 >= len(graph):
                continue
            if graph[dy2] == 0:
                graph[dy2] = graph[y] + 1
                queue.append(dy2)

            if dy1 == si or dy2 == si:
                dest_flag = True
                break
if su != si:
    bfs()
    print(graph[si])
else:
    print(0)

print(graph)