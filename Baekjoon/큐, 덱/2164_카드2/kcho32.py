import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
deq = deque(range(1, n+1))
odd = True

# while len(deq) > 1:
#     if odd:
#         deq.popleft()
#         odd = False
#     else:
#         deq.rotate(-1)
#         odd = True

# 하나 회전, 하나 버리는 식으로 카드가 1장 남을 때까지 반복
for i in range(n-1):
    deq.popleft()
    deq.rotate(-1)

print(deq[0])
