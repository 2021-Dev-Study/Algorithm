# 문제 이해 : https://hongcoding.tistory.com/20
from collections import deque
import sys
sys.setrecursionlimit(10 ** 6) # 이거 없으면 시간초과가 난다...ㅠㅜㅠ (https://kingnamji.tistory.com/39 참고)
input = sys.stdin.readline


if __name__ == "__main__":
    
    def bfs(start):
        global flag
        queue = deque()
        queue.append(start)
        visited[start] = 1 # 방문한 곳은 1

        while queue:
            v = queue.popleft()
            for i in graph[v]:
                if visited[i] == 0: # 이전에 방문하지 않은 곳이라면
                    visited[i] = -1 * visited[v] # 현재 노드와 다른 그룹 지정
                    queue.append(i)
                elif visited[v] == visited[i]: # 만약 같은 그룹이라면
                    flag = False


                   
    K = int(input())
    for _ in range(K):
        V, E = map(int,input().split())
        graph = [[] for _ in range(V+1)]
        for _ in range(E):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [0] * (V+1)
        flag = True
        for i in range(1, V+1):
            if visited[i] == 0:
                bfs(i)
        
        print('YES' if flag else 'NO')


 
        