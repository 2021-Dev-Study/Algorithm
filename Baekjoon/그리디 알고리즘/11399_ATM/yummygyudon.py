import sys
# from collections import deque
N = int(sys.stdin.readline())
# time = deque(list(map(int, sys.stdin.readline().split())))
# mn = 1e9
# for _ in range(N) :
#     ls= [0]*(N+1)
#     for i in range(N) :
#         # ls[i+1] = ls[i]+time[i]
#     print(f"time : {time}")
#     print(f"ls : {ls}")
#     mn = min(mn, sum(ls))
#     print(mn)
#     time.append(time.popleft())
# print(mn)

# 아싸 이게 더 빠르다.
time = list(map(int, sys.stdin.readline().split()))
time.sort()
ls= [0]*(N+1)
for i in range(N) :
    ls[i+1] = ls[i]+time[i]
print(sum(ls))


# 참고
s = 0
for i in range(N) :
    for k in range(i+1):
        s += time[k]
print(s)