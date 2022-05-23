if __name__ == "__main__":
    
    # find 연산을 수행하는 함수
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    # union 연산을 수행하는 함수
    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    

    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        count = 0
        
        # 루트노드를 저장하는 배열
        # 일단 자기 자신으로 초기화
        parent = [0]*(N+1)
        for i in range(1, N+1):
            parent[i] = i
        
        # 입력 받은 a,b 쌍의 루트 노드가 다른 경우에만 count 증가
        # 루트 노드가 같다면 루트 노드를 통해 a, b로 이동할 수 있다는 의미이므로 카운트하면 안됨
        for i in range(M):
            a, b = map(int, input().split())
            a = find(parent, a)
            b = find(parent, b)
            if a != b:
                count += 1
                union(parent, a, b)
        
        print(count)

