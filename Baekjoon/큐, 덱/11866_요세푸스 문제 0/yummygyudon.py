from collections import deque
## 1158 요세푸스 문제랑 한 글자도 안틀리고 다 똑같은 문제이네요..?
import sys
n, k = map(int,sys.stdin.readline().rstrip().split())
que = [int(i) for i in range(1,n+1)]
result = []
idx = 0
print("<",end='')
for i in range(n) :
    idx +=  k-1 # 번째는 실제 해당 번째 인덱스보다 1 크기 때문에
    if idx >= len(que) :
        idx = idx%len(que) # 1번째부터 n번째 => 인덱스에선 0번째부터 n-1번째 라고 생각하면 편함
        # 한 사이클이 넘어갈 때 나머지로 que 머리에서부터 셈
    result.append(que.pop(idx))
    print(f"{result[i]}", end='')
    if len(que) == 0:
        print(">")
    else:
        print(", ", end='')