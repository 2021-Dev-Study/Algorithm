
############### deque를 이용한 풀이 ############### 268
from collections import deque
N = int(input())

q = deque([])

for i in range(1,N+1):  # 1부터~ 6까지 큐에 숫자 저장 
    q.append(i)

while len(q) != 1: # 큐가 길이가 1이 아닐때 반복 
    q.popleft() # 맨 왼쪽숫자 삭제
    q.append(q.popleft()) # 맨 왼쪽 숫자 뽑아서 큐 맨뒤에 append

print(q[0]) # 큐가 길이가 1개가 되면 반복문 종료될 것이고, 남은 숫자 1개 출력 


############### 내 코드랑 비슷한 것 같은데 속도 개선한 풀이 (찾아봄) ############### 68
import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque([i for i in range(1, N + 1)])

while len(queue) > 1: # 길이가 1이상인 경우만 반복
    queue.popleft()  # 맨 처음 원소 빼줌
    queue.append(queue[0]) # 첫번째 원소를 뒤에 삽입
    queue.popleft() # 첫번째 원소 삭제 
print(queue[0]) # 길이가 1개일때 그 1개의 원소를 출력 



################ 맨 처음/ 리스트로 풀었더니 또 시간초과 남.. ################
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
