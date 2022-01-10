import sys
# 예제에서는 문제가 없군요..
# while True :
#     s = sys.stdin.readline().rstrip()
#     if s[0] == '.' :
#         break
#     stk = []
#     for chr in s :
#         stop = 0
#         if chr == '(' or chr == '[' :
#             stk.append(chr)
#         elif chr == ')' :
#             if len(stk) == 0 :
#                 print('no')
#                 stop = 1
#                 break
#             if stk[-1] == '(' :
#                 stk.pop()
#             else :
#                 print('no')
#                 break
#         elif chr == ']' :
#             if len(stk) == 0 :
#                 print('no')
#                 stop = 1
#                 break
#             if stk[-1] == '[' :
#                 stk.pop()
#             else :
#                 print('no')
#                 break
#     if len(stk)==0 and stop == 0 :
#         print('yes')

# 이건 런타임 에러... 어느 장단에 맞춰야하죠
# while True :
#     s = sys.stdin.readline().rstrip()
#     if s[0] == '.' :
#         break
#     stk = []
#     for chr in s :
#         stop = True
#         if chr == '(' or chr == '[' :
#             stk.append(chr)
#         elif chr == ')' :
#             if len(stk) == 0 :
#                 stop = False
#                 break
#             if stk[-1] == '(' :
#                 stk.pop()
#             else :
#                 stop = False
#                 break
#         elif chr == ']' :
#             if len(stk) == 0 :
#                 stop = False
#                 break
#             if stk[-1] == '[' :
#                 stk.pop()
#             else :
#                 stop = False
#                 break
#     if len(stk)==0 and stop:
#         print('yes')
#     else :
#         print('no')

# ㅋㅋㅋㅋㅋㅋㅋㅋㅋ 이건 맞았네요.. 뭐하자는 거지..
while True :
    s = sys.stdin.readline().rstrip()
    if s[0] == '.' : # 앞에 다른 내용 없이 '.'일 때, 입력 끝내기
        break
    stk = []
    for chr in s :
        stop = True
        if chr == '(' or chr == '[' : # 괄호들의 시작일 경우
            stk.append(chr) # 삽입
        # 입력값이 닫는 괄호일 때의 코드
        # ) 과 ]일때 코드는 동일하다
        elif chr == ')' :
            if len(stk) == 0 : # 만약 stk에 아무것도 없을 때, 여는 것없이 닫는 것이 나오면
                stop = False # stop을 False로 주고 break
                break
            else : # stk에 값이 있을 때
                if stk[-1] == '(' : # 직전 값이 같은 중괄호의 여는 괄호일 때 (같지 않으면 무조건 안됨)
                    stk.pop() # 해당 값을 없애주기 (stk의 길이를 결과 출력 기준으로 쓸 것이기 때문에 상관없음)
                else :
                    stop = False  # 직전 값과 다르다면 조건에 맞지않음
                    break
        elif chr == ']' :
            if len(stk) == 0 :
                stop = False
                break
            else :
                if stk[-1] == '[' :
                    stk.pop()
                else :
                    stop = False
                    break
    if len(stk)==0 and stop: # stk에 모두 짝지어져 사라지기때문에 아무것도 없으며 stop도 True일 때만
        # stop만 조건으로 사용하기엔 stop은 True인데 값 하나가 남아있을 수도 있기때문에
        print('yes')
    else :
        print('no')
