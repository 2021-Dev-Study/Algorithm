import sys

while True: # 반복 횟수가 정해지지 않아서 while문 사용
    sentance = sys.stdin.readline()
    stk = []
    if sentance[0] == ".": # 첫번째 문자로 .이 들어오면 반복문 종료
        break
    for i in range(len(sentance)):
        if (sentance[i] == "(") or (sentance[i] == "[") : # ( 거나 [이면 리스트 stk에 추가 
            stk.append(sentance[i])
            # print("append : ", stk)
        elif (sentance[i] == ")"): # )이면 
            if len(stk) != 0 and (stk[-1] == "(") : # 빈 리스트가 아니고, 리스트의 마지막 원소가 ( 일때 ( pop 해줌
                stk.pop()
                # print("pop : ", stk)
            else :  # stk가 빈 리스트라면 
                stk.append(sentance[i]) # )를 추가해준다. 어차피 )가 먼저 추가되므로 올바른 균형이 아니므로 바로 반복문 종료시킴
                break
        elif (sentance[i] == "]"): # )와 같은 원리
            if len(stk) != 0 and (stk[-1] == "[") :
                stk.pop()
                # print("pop : ", stk)
            else:
                stk.append(sentance[i])
                break 

    if len(stk) == 0: # 빈 리스트면 다 pop돼서 균형이 잡혔다는 뜻으로 올바른 균형
        print("yes")
    elif len(stk) > 0: # 0 이상이라면 , 모두 pop되지 않아 균형잡힌 문장이 아님을 판단
        print("no")
    i+=1 # i를 증가시켜 반복 계속 진행



######################### 풀고나서 찾아본 풀이 ######################### 
# True / False로 하는 점이 인상 깊었고, 길이로 0을 판단하는 것이 아닌 not연산자?로 빈 리스트를 판단하는 점도 새로웠음

while True:
    s = input()
    if s == '.':
        break
    stk = []
    temp = True
    for i in s:
        if i == '(' or i == '[':
            stk.append(i)
        elif i == ')':
            if not stk or stk[-1] == '[':
                temp = False
                break
            elif stk[-1] == '(':
                stk.pop()
        elif i == ']':
            if not stk or stk[-1] == '(':
                temp = False
                break
            elif stk[-1] == '[':
                stk.pop()
    if temp == True and not stk:
        print('yes')
    else:
        print('no')