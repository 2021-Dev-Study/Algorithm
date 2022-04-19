import sys
computer = int(sys.stdin.readline())
n = int(sys.stdin.readline())

graph=[[]*(computer+1) for _ in range(computer+1)]
visited = [0] * (computer + 1)

result = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b) # 연관된 노드들 리스트에 넣어 줌 
    graph[b].append(a)

# graph :  [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

def dfs(num):
    global result
    visited[num] = 1

    for i in graph[num]:
        if visited[i] == 0:
            result += 1 # 처음 방문 하면 컴퓨터 개수 1개 추가 
            dfs(i) # i를 넘겨서 재귀로 호출. i를 방문 처리 해줌 

    return result

print(dfs(1)) # 1부터 시작