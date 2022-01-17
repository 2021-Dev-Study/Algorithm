from collections import deque
N = int(input())

q = deque([])

for i in range(1,N+1):
    q.append(i)
print(q)
print("길이:",len(q))
while len(q) != 1:
    q.popleft()
    print("큐 처음 숫자 팝 :",q)
    q.append(q.popleft())
    print("큐 팝한 뒤 첫번째 숫자 팝 어펜드 :",q)
print(q[0])