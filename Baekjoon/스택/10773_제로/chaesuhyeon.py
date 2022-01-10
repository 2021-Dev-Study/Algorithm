import sys

K = int(sys.stdin.readline())
stk = []

for k in range(K):
    num = int(sys.stdin.readline())
    if num == 0: # 입력 받은 숫자가 0일 경우
        if len(stk) == 0: #  예외 처리를 안해주면 처음 입력 받은 숫자가 0일 경우 뺄 숫자가 없어서 index error 발생   
            try :
                continue  # 오류 발생하면 그냥 반복문 처음부터 진행
            except :
                IndexError
        else:
            stk.pop() # 빈 리스트가 아니라면 , 마지막 단어 pop해줌
    else:
        stk.append(num) # 입력 받은 숫자가 0이 아닐 경우 그냥 리스트에 추가해줌
print(sum(stk)) # 리스트 각 요소의 합 출력



# 처음에는 다 입력 받아서 리스트 먼저 생성 후 index 거꾸로 하면서 체크해주는 방법.. 근데 0이 또 나올 경우를 코드 못짜겠음..

# for k in range(1, K+1):
#     num = int(sys.stdin.readline())
#     stk.append(num)

# for i in range(K, 1, -1):
#     if stk[i] == 0 :
#         if stk[i-1] != 0:
#             stk.pop(stk[i-1])
#         else:
#             if stk[i-2] !=0:
#                 stk.pop(stk[i-2])
#     else :
#         continue
