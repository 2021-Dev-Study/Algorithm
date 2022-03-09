import sys
N = int(sys.stdin.readline())
people = [None]*N
for i in range(N) :
    people[i] = list(map(int, sys.stdin.readline().split()))

# 이건 너무 쉬웠으니 퓰이 생략
for b in people :
    rank = 1
    for v in people :
        if b[0] < v[0] and b[1] < v[1] :
            rank += 1
    print(rank,end=' ')
