# 12873 : 기념품

from collections import deque

n = int(input())
deq = deque(range(1, n+1))

# 1, n까지만 하면 덱에는 1개의 수만 남게 됨
for i in range(1, n):
    n_rot = (i ** 3 - 1) % len(deq) # t^3에서 회전하고 남은 나머지
    deq.rotate(-n_rot)              # 나머지 만큼 회전하고
    deq.popleft()                   # 그 앞사람 제거

print(deq[0])


'''
n=int(input())
a=[*range(1,1+n)]
p=0
for i in range(1,n):a.pop(p:=(p+i**3-1)%len(a))
print(*a)
'''