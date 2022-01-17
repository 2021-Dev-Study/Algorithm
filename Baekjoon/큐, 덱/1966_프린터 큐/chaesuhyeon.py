# 처음 풀이는 M(궁금한 문서의 인덱스)의 값가지고 pop한 값과 대소비교를 해서 cnt를 측정하여 cnt를 측정하려고 했으나.. 
# 3번째 예제처럼 같은 값이 있을때 정확한 비교를 할 수가 없음
# 인덱스를 저장한 큐도 생성하여 중요도 큐와 같이 이동


import sys
from collections import deque
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    N , M = map(int, sys.stdin.readline().rstrip().split())
    I = deque(list(map(int, sys.stdin.readline().rstrip().split()))) # 중요도 저장하는 큐 
    idx = deque(list(range(N))) # 인덱스 저장하는 큐 
    cnt = 0
    while I:
        if I[0] == max(I): # 큐의 첫번째 값이 가장 높은 중요도라면 
            I.popleft() # 그 값을 삭제하고 
            cnt += 1 # 카운트 올려줌 
            ip = idx.popleft() # 최댓값에 맞는 인덱스도 pop해준다음 ip에 저장 
            if ip == M: # 최댓값의 인덱스가 M(궁금한 문서의 인덱스)과 같다면 cnt바로 출력 후 반복문 종료  
                print(cnt)
                break
        else: # 큐의 첫번째 값이 최댓값이 아니라면 
            I.append(I.popleft()) # 첫번째 값을 pop해준뒤 다시 append
            idx.append(idx.popleft()) # 인덱스도 함께 움직여줘야 하므로 인덱스도 pop해주고 append


######################## 처음 풀이 ! 숫자로 비교했는데 이렇게 하니까 1 1 9 1 1 1을 계산을 못함
# import sys
# from collections import deque
# t = int(sys.stdin.readline().rstrip())
# for _ in range(t):
#     N , M = map(int, sys.stdin.readline().rstrip().split())
#     I = deque(list(map(int, sys.stdin.readline().rstrip().split())))
#     cnt = 0
#     paper = I[M]
#     max_num = max(I)
#     while True:
#         p = I.popleft()
#         if p < paper :
#             I.append(p)
#         elif p > paper:
#             cnt+=1
#         elif p == paper:
#             if max_num in I:
#                 I.append(p)
#             else:
#                 cnt+=1
#                 break
#     print(cnt)
        



