
############### deque를 이용한 풀이 ###############

import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque([i for i in range(1, N + 1)])

while len(queue) > 1: # 길이가 1이상인 경우만 반복
    queue.popleft()  # 맨 처음 원소 빼줌
    queue.append(queue[0]) # 첫번째 원소를 뒤에 삽입
    queue.popleft() # 첫번째 원소 삭제 
print(queue[0]) # 길이가 1개일때 그 1개의 원소를 출력 



################ 리스트로 풀었더니 또 시간초과 남.. ################
# import sys

# N = int(sys.stdin.readline())
# cnt = 1
# idx = 0
# queue = []
# while cnt <= N :
#     queue.append(cnt)
#     cnt += 1
# while True:
#     queue = queue[1:]
#     if len(queue) == 1:
#         print(queue[0])
#         break
#     else:

#         queue.append(queue[0])
#         queue = queue[1:]


################ 두번째 풀이 - deque이용 런타임 에러 ################
# import sys
# from collections import deque
# queue = deque([])
# N = int(sys.stdin.readline())
# cnt = 1

# while cnt <= N :
#     queue.append(cnt)
#     cnt += 1
# while True:           ###### 이 반복문 안에서  if문을 써서 런타임 에러 난 것 같음 
#     queue.popleft()
#     if len(queue) == 1:
#         print(queue[0])
#         break
#     else:

#         queue.append(queue[0])
#         queue.popleft()