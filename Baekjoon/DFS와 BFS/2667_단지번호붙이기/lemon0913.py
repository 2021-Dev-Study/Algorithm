import sys
if __name__ == "__main__":
    N = int(input())
    graph = []
    for i in range(N):
        graph.append(list(map(int, sys.stdin.readline().replace('\n', ''))))


    def dfs(x, y):
        # 주어진 범위를 벗어나면 종료
        if x < 0 or y < 0 or x >= N or y >= N:
            return False
        # 현재 노드를 방문하지 않았다면
        if graph[x][y] == 1:
            # count는 1 증가
            global count
            count += 1
            # 방문 처리 하기
            graph[x][y] = 0

            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x, y+1)
            return True
        return False

    result = 0 # 단지 수
    count = 0 # 단지 내의 집의 수
    num = [] # 단지 내의 집의 수를 저장하는 리스트
    for i in range(N):
        for j in range(N):
            if dfs(i, j) == True:
                num.append(count) 
                result += 1 # 단지 수 1 증가
                count = 0 # 단지 내의 집의 수는 리셋하기

    num.sort()
    print(result)
    for i in num:
        print(i)