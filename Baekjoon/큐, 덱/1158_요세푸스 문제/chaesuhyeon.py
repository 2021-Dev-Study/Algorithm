# 생각했던 아이디어 --> 1 2 3 4 5 6 7 에서 3을 뽑고나면 이때부터 또 3개씩 이므로 인덱스 계산해주기 귀찮아서 
# 뽑은 숫자 다음 숫자를 첫번째로 오게 만듦 (그 앞에 숫자들은 뒤로 붙임)
# 4 5 6 7 1 2 (그다음 6제거)
# 7 1 2 4 5 이런식으로.. 여기까지 생각했는데 구현하는데서 코드가 계속 막혀서 나랑 아이디어 똑같은 풀이를 참고함  
# 근데 시간 진짜 오래걸리는 풀이..라서 인덱스 풀이 봄
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


#################################
N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
answer = []
idx = 0
for i in range(N):
  idx += K-1
  print("idx 처음 : ",idx)
  if idx >= len(arr):
    idx %= len(arr)
    print("idx 나눈 후 : ",idx)
  answer.append(str(arr.pop(idx)))
  print("answer : ",answer)
print('<', ', '.join(answer), '>', sep='')