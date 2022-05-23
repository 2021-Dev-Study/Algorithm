# 책이랑 똑같이 풀면 된다
if __name__ == "__main__":

    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]
    
    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b


    V, E = map(int, input().split())
    parent = [0] * (V+1)
    for i in range(1, V+1):
        parent[i] = i
    
    edges = []
    result = 0

    for _ in range(E):
        a, b, c = map(int, input().split())
        edges.append((c,a,b))
    
    edges.sort()

    for e in edges:
        c, a, b = e
        a = find(parent, a)
        b = find(parent, b)
        if a != b:
            result += c
            union(parent, a, b)
        
    print(result)