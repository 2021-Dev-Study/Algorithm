import sys
from collections import deque
# 이거 큐 문제 맞나요...?
n = int(sys.stdin.readline().rstrip())
queue = deque([i for i in range(1, n+1)])
result = []
while True :
    result.append(queue.popleft()) # 첫번째 값 result에 삽입
    if not queue : # queue.append(queue.popleft()) 에서 스스로 popleft할 값이 없으면 오류
        break
    queue.append(queue.popleft())# 두번째 값을 pop해서 다시 뒤에 삽입
for num in result :
    print(num, end=' ')



