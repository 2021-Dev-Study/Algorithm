#풀이 봤슴덩..
import sys
from collections import deque

stk = [] ## 괄호 밖 문자 저장 
q=deque() ## 괄호 안의 문자
result = '' ## 총 결과값
state = True ## true = 뒤집어서 출력 / false : 안뒤집음

S = sys.stdin.readline().rstrip()

for i in S:
    if i == "<": # "<" 괄호가 나올때
        while stk: # 만약 괄호 밖의 문자가 존재한다면
            result += stk.pop() # 현재 있는 결과에 거꾸로 출력 
        q.append(i) # "<" 괄호 큐에 append
        state = False # 괄호 안이라는 상태표시. 뒤집을 필요 없는 상태
    
    elif i == ">": # ">" 괄호가 나오면
        q.append(i) # 큐에 닫는 괄호 append
        state = True # 괄호가 끝났기 때문에 다시 뒤집을 필요가 있다는 상태표시를 해줌
        while q : # 괄호부터 괄호 안에있는 문자를 결과값에 저장
            result += q.popleft() # popleft()를 이용하여 왼쪽부터 pop
    
    elif i==' ': # i가 공백문자라면
        if state: # 괄호 밖일 때 (state = True)
            while stk: # 스택이 존재할때까지  
                result += stk.pop() # 이제까지 스택에 저장된 문자들을 pop해줘서 거꾸로 만들어주고 결과값에 저장
            result += ' '  # 문자를 뒤집어서 출력해준 뒤 결과값에 공백 추가 
        else: # 괄호 안이라면
            q.append(i) # 그냥 공백문자 추가해줌
            while q: # 큐가 존재한다면 존재하는 동안 result에 문자 저장 
                result += q.popleft() #
    else: # i가 괄호, 공백이 아닌 문자일때
        if state: # 만약 괄호 밖이라면 (state = True)
            stk.append(i) # 스택에 추가해줌 
        else: # 괄호 안이라면
            q.append(i) # 큐에 추가해줌
while stk: # 혹시 스택에 남아있는 문자가 있다면 (마지막이 문자라면 추가만 될 뿐 pop해서 빼주는 과정이 빠졌기 때문에 pop해준다)
    result += stk.pop() # 모두 결과값에 저장
 
print(result) # 최종 결과 출력 

    
    







