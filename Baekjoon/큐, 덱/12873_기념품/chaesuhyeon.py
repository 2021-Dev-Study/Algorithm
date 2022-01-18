N = int(input())
idx = 0
step = 1
q = [i for i in range(1,N+1)]

while True:
    t = step ** 3
    idx += t - 1 # 그 숫자부터 이어서 게임이 흘러가므로 누적
    if len(q) == 1: # q가 원소가 1개있으면 반복문 종료 
        break
    if idx > len(q): # idx가 길이를 초과하면 idx를 q길이로 나눠줌
        idx %= len(q)
    q.pop(idx) # 그 인덱스에 맞는 숫자 pop
    step += 1 # 단계 하나 올려줌 

print(q[0])

#########
# from collections import deque

# N = int(input())
# idx = 0
# step = 1
# q = deque([i for i in range(1,N+1)])
# while True:
#     t = step ** 3
#     print("t", t)
#     if t == 1:
#         q.popleft()
#         print("q - 1제거", q)
#     else:
#         for _ in range(t):
#             qp =q.popleft()
#             q.append(qp)
#             print("q after append", q)
#         q.pop()
#         print("q after pop", q)
#     step += 1
#     if len(q) == 1:
#         break
# print(q)
# print(q[0])