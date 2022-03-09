from collections import deque
import time
t1 = time.time()
A, B = map(int, input().split())
q = deque()

left = right = 0
q.append([1,1, left, right])
while q :
    a, b, l, r = q.popleft()
    if a > A or b > B :
        continue
    if a==A and b==B :
        print(f"{l} {r}")
        break
    q.append([a+b, b, l+1, r])
    q.append([a, a+b, l, r+1])

    # 이게 더 길어요... 2.036534309387207
    # if a < A :
    #     q.append([a+b, b, l+1, r])
    # elif b < B :
    #     q.append([a, a+b, l, r+1])
t2 = time.time()
print(t2-t1)
# 음.. 1.2673194408416748 가 걸리네요... 시간초과..