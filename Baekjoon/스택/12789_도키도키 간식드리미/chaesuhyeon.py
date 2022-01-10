# 검색해보니 큐와 스택이 섞여있는 문제
# 풀이 봤음..ㅎㅎ..

from collections import deque
n = int(input())
num = deque(map(int, input().split()))
stk = deque([])
cnt = 1
while num :
    if num[0] == cnt: # 첫번째 숫자가 cnt와 같으면 pop해줌
        num.popleft() # 맨 처음 숫자 빼줌 
        cnt += 1
    else:
        stk.append(num.popleft()) # cnt와 같지 않으면 빼주고 스택에 append
    
    while stk: # 스택이 존재한다면
        if stk[-1] == cnt: # 스택의 마지막 데이터와 cnt가 같으면 stk에서 제거 
            stk.pop()
            cnt+=1
        else: # 스택의 마지막 원소와cnt가 같지 않은 경우는 반복문 종료 
            break
if len(stk) == 0:
    print('Nice')
else:
    print('Sad')





# import sys
# n = int(input())
# num = list(map(int, sys.stdin.readline().split() ))
# stk1 = []
# stk2=[]
# i=0
# while i <= n:
#     if len(stk1) == 0 or len(stk2)==0:
#         if num[i] == min(num):
#             stk1.append(num[i])
#         else:
#             stk2.append(num[i])
#     else:
#         if stk2[-1] - num[i] == 1 :
#             stk2.append(num[i])
#         elif stk2[-1] - stk1[-1] == 1:
#             stk1.append(stk2.pop())
#         else:
#             print("Sad")
#         i += 1
# while True:
#     if stk2:
#         stk1.append(stk2.pop())
#     else:
#         break
# for i in range(len(stk1)-1):
#     if stk1[i+1] - stk1[i] == 1:
#         print("Nice")
#     else:
#         print("Sad")





    




    







