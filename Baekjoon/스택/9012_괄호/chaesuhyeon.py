# 리스트가 빈 경우에 )가 나오면 계속 오류가 발생해서 
# try문을 써줬는데 예외 처리를 해주면 계속 빈리스트여서 결국 리스트 길이0이됨.. 
# 그렇게 되면 올바른 괄호 처리가 돼서 15~18라인 부분만 풀이참고..

import sys
T = int(sys.stdin.readline())
for t in range(T):
    ps = sys.stdin.readline()
    stk =[]

    for i in ps:
        if i == "(": # 문자열 하나씩 for문 돌려서 보는데 i 가 ( 라면 리스트 stk에 추가한다
            stk.append(i)
        elif i == ")": # i 가 ( 일 경우에 , 리스트가 빈 리스트가 아니고, 리스트의 마지막 원소값이 ( 일경우에 pop해줌 
            if len(stk) != 0 and stk[-1] == "(":
                stk.pop()
            else: # len(stk) == 0 and stk[-1] == ")" 일 경우에는 어차피 빈 리스트에 원소가 )라는 말은 올바른 괄호가 아니라는 말
                stk.append(i) # 추가를 해줘서 빈 리스트가 아니도록 만듦 (어차피 올바른 괄호가 아니라서)

    if len(stk) == 0 :
        print("YES")

    elif len(stk) > 0:
        print("NO")
            
  


# 처음에는 왼쪽 괄호, 오른쪽 괄호 개수로 접근했다가 실패 
# for t in range(T):
#     left = [] # 왼쪽 괄호 ( 
#     right = [] # 오른쪽 괄호 )
#     ps = list(sys.stdin.readline())
#     for i in ps:
#         if i == "(":
#             left.append(i)
#         elif i == ")":
#             right.append(i)
#     print("left : ",len(left))
#     print("right : ",len(right))
#     if len(left) == len(right) :
#         print("YES")
#     else:
#         print("NO")
