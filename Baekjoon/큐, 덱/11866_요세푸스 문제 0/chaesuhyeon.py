from collections import deque
N , K = map(int, input().split())
q = deque([])

for i in range(1,N+1):
    q.append(i)   # 1 ~ 7까지 큐에 추가 

print('<', end='')
while q: # 큐가 존재하는 동안 
    for i in range(K-1): # 두번째 숫자까지 추가하고 빼준다음에 
        q.append(q[0])
        q.popleft() 
    print(q.popleft() , end='') # 세번째 숫자를 빼고 출력해줌 end를 써서 이어서 출력 
    if q: # 큐가 존재한다면 ,를 써서 출력 형식 맞춰주기 
        print(', ', end='')
print('>')        # 큐가 다 pop돼서 while문이 종료되면 >출력해줌 


