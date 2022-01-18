from collections import deque
import sys
n = int(sys.stdin.readline())
que = deque([i for i in range(1,n+1)])

# ... 232ms....너무 오래걸리는데
while len(que) > 1 :
    que.popleft()
    que.append(que.popleft())

print(que[0])

# 320ms.... deque를 애용합시다~
# ls = [i for i in range(1,n+1)]
# start = 0
# rear = no = n
#
# while no > 1 :
#     ls[start] = None
#     ls.append(ls[start+1])
#     no -= 1
#     start+=2
#     rear += 1
# print(ls[rear-1])