import sys
input = sys.stdin.readline
N, R, start = map(int,input().split())

Node = [[]for _ in range(N+1)]
visited = [False]*(N+1)
for _ in range(R) :
    s, e = map(int, input().split())
    Node[s].append(e)
    Node[e].append(s)

for i in range(len(Node)) :
    Node[i].sort()

def dfs(Node, visited, n) :
    visited[n] = True
    print(n, end=' ')
    for i in Node[n] :
        if visited[i] == False :
            dfs(Node, visited, i)
dfs(Node,visited, start)

print()

from collections import deque

q = deque()
visited = [False]*(N+1)
q.append(start)
while q :
    s_Node = q.popleft()
    if visited[s_Node] == True :
        continue
    print(s_Node, end = ' ')
    visited[s_Node] = True
    for i in Node[s_Node] :
        q.append(i)