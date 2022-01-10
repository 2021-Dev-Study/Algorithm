# 17952	: 과제는 끝나지 않아! silver_4
'''
너무나도 많은 과제를 하다가 미쳐버린 성애...

1. 과제는 가장 최근에 나온 순서대로 한다. 또한 과제를 받으면 바로 시작한다.
2. 과제를 하던 도중 새로운 과제가 나온다면, 
    하던 과제를 중단하고 새로운 과제를 진행한다.
3. 새로운 과제가 끝났다면, 이전에 하던 과제를 이전에 하던 부분부터 이어서 한다. 
    (아무리 긴 시간이 지나도 본인이 하던 부분을 기억할 수 있다.)

과제를 받자마자 이 과제가 몇 분이 걸릴지 정확하게 알 수 있고, 
제출한 과제는 무조건 만점을 받는다. 받을 과제 점수?
'''
# 시간초과 pypy3로 해결 

n = int(input())
stk = []
score = 0

for i in range (n):
    assignments = list(map(int, input().split()))
    
    if assignments[0] == 1:
        stk.append([assignments[1], assignments[2]]) # [과제, 시간] 스택에 넣음
    
    if stk:
        stk[-1][1] -= 1  # 최신 과제 시간부터 생각해야 함
        if stk[-1][1] == 0:
            score += stk[-1][0]
            stk.pop()
print(score)

'''
score = 0
time = 0
for i in stk[::-1]:
  if time < n-1:
    score += i[0]
    time += i[1]
print(score) 
'''


