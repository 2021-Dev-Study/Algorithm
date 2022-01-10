import sys
S = sys.stdin.readline().rstrip()

stk1 = [] # "("만 담는 스택
stk2=[] # ")"만 담는 스택 

for i in S: # 문자열 하나하나 반복문 돌려봄 
    if i == "(":
        stk1.append("(") # 여는 괄호이면 stk1에 append
    else: # 닫는 괄호이면 
        if stk1: # stk1이 빈 리스트가 아니라면 (stk1이 빈 리스트일 경우에는 pop실행x )    
            stk1.pop()
        else: # stk1가 빈 리스트가 아니면 여는 괄호가 없다는 뜻이기 때문에 여는괄호 필요함 -> 개수 측정해 주기위해 stk2에 append
            stk2.append(")")
print(len(stk2)+len(stk1)) # 없애지 못한 각 괄호들의 개수를 구해줌 (짝이 필요한 괄호들의 개수)
            



    







