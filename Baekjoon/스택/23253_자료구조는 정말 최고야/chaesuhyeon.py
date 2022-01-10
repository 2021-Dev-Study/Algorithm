# 막대기 문제랑 비슷한 것 같다.
# 내림차순 아이디어 얻고 스택으로 다시 풀이 
# 모든 더미가 내림차순으로 정렬이 되어 있는 상태여야함

import sys
N, M = map(int, sys.stdin.readline().rstrip().split())

status = True # 상태 체크를 위한 변수 

for _ in range(M):
    stk = [] # 스택 초기화 
    num = sys.stdin.readline() # 한 더미의 책 개수 
    book= list(map(int, sys.stdin.readline().rstrip().split())) # 책 번호 입력 
    
    while book: # 책이 존재하는 동안 
        for i in range(len(book)): # 책의 개수만큼 반복 
            if stk: # 만약에 스택이 존재한다면 
           
                if stk[-1] < book[-1]: # 스택의 마지막 데이터와 책의 마지막 데이터를 비교했을 때 책의 번호가 더 크다면 pop 해줌 
                    stk.append(book.pop()) # 스택에 append해줌
                
                else: # 만약에 스택에 있는 책 번호가 더 크다면 정렬실패 
                    status = False # 실패했으니 상태 false
                 
            else: # 빈 스택이라면 데이터 추가 (맨처음에는 스택이 비어있기 때문에 데이터 넣어줘야함)
                stk.append(book.pop())
                
        if status == False: # for문을 다 돌았는데 상태가 여전히 false라는 것은 정렬에 실패했다는 것
            break # 반복문 더 진행할 필요가 없음(뒤에 숫자(책번호)가 더 남았을 경우에 해당)
   
    if status == False: # while문이 종료됐는데 상태가 false라면 내림차순이 안되는 부분이 있었다는 뜻
        continue

if status == True: # 반복문 다 끝났는데 false가 한부분도 없어서 다 true가 나왔다면 yes
    print("Yes")
else : # false가 나왔다는건 더미 중 내림차순이 아닌 더미가 있었다는 뜻이므로 no
    print("No")




#########################################   스택 이용 안하는 방법 - 다른 사람 풀이 내방식으로 조금 변경 
# import sys
# N, M = map(int, sys.stdin.readline().split())

# status = True

# for _ in range(M):
#     num = sys.stdin.readline()
#     book= list(map(int, sys.stdin.readline().split())) # [[3, 1], [4, 2]]
#     for i in range(len(book)-1):
#         if (book[i] - book[i+1]) < 0 :
#             status = False
#             break

# if status == True:
#     print("Yes")
# else :
#     print("No")




#########################################   스택 맨 처음 풀이 : 시간초과 (2차원 배열로 풀었음)

# import sys
# N, M = map(int, sys.stdin.readline().split())

# book = []
# stk = []
# status = True

# for i in range(N, 0, -1):
#     stk.append(str(i))
# print("처음 stk : ", stk)

# for _ in range(M):
#     num = sys.stdin.readline()
#     book.append(sys.stdin.readline().split()) # [[3, 1], [4, 2]]

# print("book : " , book)

# while stk:
#     s = stk.pop()
#     print("s : " , s)
#     for i in range(len(book)):
#         if book[i]:
#             if s == book[i][-1]:
#                 book[i].pop()
#                 status = True
#                 print("book pop : " , book)
#                 break
#             else:
#                 status = False
#                 print("book 실패 : " , book)

#     if status == False:
#         print("No")
#         break
# if status == True:
#     print("Yes")    








    







